import openai
from typing import Dict, Any, Optional, List
import os
import logging
import asyncio

class CodeGenerator:
    """
    Gerador de código usando IA
    Suporta múltiplas linguagens e frameworks
    """
    
    def __init__(self, openai_client=None):
        self.openai_client = openai_client or openai
        self.logger = logging.getLogger(__name__)
        
        # Templates de código para diferentes linguagens
        self.templates = {
            "python": {
                "function": "def {name}({params}):\n    \"\"\"{docstring}\"\"\"\n    {body}",
                "class": "class {name}:\n    \"\"\"{docstring}\"\"\"\n    \n    def __init__(self{params}):\n        {init_body}\n    \n    {methods}",
                "test": "import unittest\nfrom {module} import {function}\n\nclass Test{function}(unittest.TestCase):\n    {test_methods}\n\nif __name__ == '__main__':\n    unittest.main()"
            },
            "javascript": {
                "function": "/**\n * {docstring}\n */\nfunction {name}({params}) {\n    {body}\n}",
                "class": "/**\n * {docstring}\n */\nclass {name} {\n    constructor({params}) {\n        {init_body}\n    }\n    \n    {methods}\n}",
                "test": "const { {function} } = require('./{module}');\n\ndescribe('{function}', () => {\n    {test_methods}\n});"
            }
        }
    
    def generate_code(
        self, 
        prompt: str,
        language: str = "python",
        framework: Optional[str] = None,
        include_comments: bool = True,
        include_tests: bool = False,
        style: str = "clean"
    ) -> str:
        """
        Gera código baseado no prompt fornecido
        
        Args:
            prompt: Descrição do código a ser gerado
            language: Linguagem de programação
            framework: Framework específico (opcional)
            include_comments: Se deve incluir comentários
            include_tests: Se deve incluir testes
            style: Estilo do código (clean, minimal, documented)
            
        Returns:
            Código gerado como string
        """
        try:
            # Constrói o prompt do sistema
            system_prompt = self._build_system_prompt(
                language, framework, include_comments, include_tests, style
            )
            
            # Chama a API OpenAI
            response = self.openai_client.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=2000
            )
            
            code = response.choices[0].message.content.strip()
            
            # Remove marcadores de código se presentes
            if code.startswith("```"):
                lines = code.split("\n")
                code = "\n".join(lines[1:-1])
            
            self.logger.info(f"Code generated successfully for language: {language}")
            return code
            
        except Exception as e:
            self.logger.error(f"Error generating code: {str(e)}")
            raise Exception(f"Failed to generate code: {str(e)}")
    
    async def generate_code_async(self, *args, **kwargs) -> str:
        """Versão assíncrona da geração de código"""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.generate_code, *args, **kwargs)
    
    def _build_system_prompt(
        self, 
        language: str, 
        framework: Optional[str], 
        include_comments: bool, 
        include_tests: bool,
        style: str
    ) -> str:
        """Constrói o prompt do sistema para geração de código"""
        
        base_prompt = f"""
        Você é um expert em programação especializado em {language}.
        Gere código de alta qualidade, limpo e funcional.
        
        Diretrizes:
        - Use as melhores práticas de {language}
        - Código deve ser produção-ready
        - Siga padrões de nomenclatura da linguagem
        """
        
        if framework:
            base_prompt += f"- Use o framework {framework} quando apropriado\n"
        
        if include_comments:
            base_prompt += "- Inclua comentários explicativos\n"
            
        if include_tests:
            base_prompt += "- Inclua testes unitários\n"
        
        style_guidelines = {
            "clean": "- Foque em código limpo e legível",
            "minimal": "- Seja conciso e minimalista", 
            "documented": "- Inclua documentação detalhada"
        }
        
        base_prompt += f"{style_guidelines.get(style, '')}\n"
        base_prompt += "\nResponda APENAS com o código, sem explicações adicionais."
        
        return base_prompt
    
    def generate_function(
        self,
        function_name: str,
        description: str,
        parameters: List[Dict[str, str]],
        language: str = "python",
        return_type: Optional[str] = None
    ) -> str:
        """
        Gera uma função específica
        
        Args:
            function_name: Nome da função
            description: Descrição da funcionalidade
            parameters: Lista de parâmetros com tipo e descrição
            language: Linguagem de programação
            return_type: Tipo de retorno
            
        Returns:
            Código da função gerada
        """
        
        params_str = ", ".join([f"{p['name']}: {p.get('type', 'Any')}" for p in parameters])
        
        prompt = f"""
        Crie uma função chamada '{function_name}' que {description}.
        
        Parâmetros:
        {self._format_parameters(parameters)}
        
        {"Retorna: " + return_type if return_type else ""}
        
        A função deve ser robusta, incluir validação de entrada e tratamento de erros.
        """
        
        return self.generate_code(prompt, language)
    
    def generate_class(
        self,
        class_name: str,
        description: str,
        methods: List[Dict[str, Any]],
        language: str = "python"
    ) -> str:
        """
        Gera uma classe completa
        
        Args:
            class_name: Nome da classe
            description: Descrição da classe
            methods: Lista de métodos a serem implementados
            language: Linguagem de programação
            
        Returns:
            Código da classe gerada
        """
        
        methods_desc = "\n".join([
            f"- {method['name']}: {method['description']}" 
            for method in methods
        ])
        
        prompt = f"""
        Crie uma classe chamada '{class_name}' que {description}.
        
        A classe deve ter os seguintes métodos:
        {methods_desc}
        
        Implemente todos os métodos com funcionalidade completa.
        Inclua construtor apropriado e docstrings.
        """
        
        return self.generate_code(prompt, language, include_comments=True)
    
    def _format_parameters(self, parameters: List[Dict[str, str]]) -> str:
        """Formata lista de parâmetros para o prompt"""
        formatted = []
        for param in parameters:
            line = f"- {param['name']}"
            if 'type' in param:
                line += f" ({param['type']})"
            if 'description' in param:
                line += f": {param['description']}"
            formatted.append(line)
        return "\n".join(formatted)
    
    def explain_code(self, code: str, language: str = "python") -> str:
        """
        Explica um código fornecido
        
        Args:
            code: Código a ser explicado
            language: Linguagem do código
            
        Returns:
            Explicação detalhada do código
        """
        
        prompt = f"""
        Explique este código {language} de forma detalhada:
        
        ```{language}
        {code}
        ```
        
        Inclua:
        - O que o código faz
        - Como funciona cada parte
        - Possíveis melhorias
        - Casos de uso
        """
        
        try:
            response = self.openai_client.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um expert em análise de código."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            self.logger.error(f"Error explaining code: {str(e)}")
            return f"Erro ao explicar o código: {str(e)}"
    
    def optimize_code(self, code: str, language: str = "python") -> Dict[str, str]:
        """
        Otimiza um código fornecido
        
        Args:
            code: Código a ser otimizado
            language: Linguagem do código
            
        Returns:
            Dict com código otimizado e explicação das melhorias
        """
        
        prompt = f"""
        Otimize este código {language} melhorando performance, legibilidade e práticas:
        
        ```{language}
        {code}
        ```
        
        Retorne apenas o código otimizado, sem explicações.
        """
        
        try:
            optimized_code = self.generate_code(prompt, language)
            
            # Gera explicação das melhorias
            explanation_prompt = f"""
            Compare estes dois códigos e explique as melhorias:
            
            ORIGINAL:
            ```{language}
            {code}
            ```
            
            OTIMIZADO:
            ```{language}
            {optimized_code}
            ```
            """
            
            response = self.openai_client.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Explique as otimizações realizadas."},
                    {"role": "user", "content": explanation_prompt}
                ],
                temperature=0.3
            )
            
            return {
                "optimized_code": optimized_code,
                "improvements": response.choices[0].message.content
            }
            
        except Exception as e:
            self.logger.error(f"Error optimizing code: {str(e)}")
            return {
                "optimized_code": code,
                "improvements": f"Erro ao otimizar: {str(e)}"
            }
