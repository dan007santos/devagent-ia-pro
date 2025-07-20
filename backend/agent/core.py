import os
import openai
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
import logging

load_dotenv()

class DevAgent:
    """
    Classe principal do DevAgent IA Pro
    Responsável por coordenar todas as funcionalidades do agente autônomo
    """
    
    def __init__(self):
        self.openai_client = None
        self.logger = self._setup_logger()
        self._initialize_openai()
        self.capabilities = {
            "code_generation": True,
            "telegram_bots": True,
            "trading": True,
            "image_generation": True,
            "youtube_upload": True
        }
    
    def _setup_logger(self) -> logging.Logger:
        """Configura o sistema de logs"""
        logger = logging.getLogger("DevAgent")
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def _initialize_openai(self):
        """Inicializa o cliente OpenAI"""
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            openai.api_key = api_key
            self.openai_client = openai
            self.logger.info("OpenAI client initialized successfully")
        else:
            self.logger.warning("OpenAI API key not found")
    
    async def process_request(self, request_type: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processa uma solicitação do usuário
        
        Args:
            request_type: Tipo da solicitação (code, bot, trade, image, youtube)
            params: Parâmetros específicos da solicitação
            
        Returns:
            Resultado processado
        """
        try:
            if request_type == "code_generation":
                return await self._handle_code_generation(params)
            elif request_type == "telegram_bot":
                return await self._handle_telegram_bot(params)
            elif request_type == "trading":
                return await self._handle_trading(params)
            elif request_type == "image_generation":
                return await self._handle_image_generation(params)
            elif request_type == "youtube_upload":
                return await self._handle_youtube_upload(params)
            else:
                return {"error": f"Unknown request type: {request_type}"}
                
        except Exception as e:
            self.logger.error(f"Error processing request: {str(e)}")
            return {"error": str(e)}
    
    async def _handle_code_generation(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com solicitações de geração de código"""
        from ..generators.code_generator import CodeGenerator
        
        generator = CodeGenerator(openai_client=self.openai_client)
        result = await generator.generate_code_async(
            prompt=params.get("prompt"),
            language=params.get("language", "python"),
            framework=params.get("framework"),
            include_comments=params.get("include_comments", True),
            include_tests=params.get("include_tests", False)
        )
        
        return {"success": True, "code": result}
    
    async def _handle_telegram_bot(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com criação/gerenciamento de bots Telegram"""
        from ..bots.telegram_bot import TelegramBotManager
        
        bot_manager = TelegramBotManager()
        
        if params.get("action") == "create":
            result = await bot_manager.create_bot_async(
                name=params.get("name"),
                token=params.get("token"),
                features=params.get("features", {})
            )
        elif params.get("action") == "start":
            result = await bot_manager.start_bot(params.get("bot_id"))
        elif params.get("action") == "stop":
            result = await bot_manager.stop_bot(params.get("bot_id"))
        else:
            result = {"error": "Unknown bot action"}
        
        return result
    
    async def _handle_trading(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com operações de trading"""
        from ..integrations.trading_manager import TradingManager
        
        trading_manager = TradingManager()
        
        if params.get("action") == "create_strategy":
            result = await trading_manager.create_strategy(
                exchange=params.get("exchange"),
                pair=params.get("pair"),
                strategy_type=params.get("strategy_type"),
                params=params.get("strategy_params")
            )
        elif params.get("action") == "execute_trade":
            result = await trading_manager.execute_trade(
                exchange=params.get("exchange"),
                pair=params.get("pair"),
                side=params.get("side"),
                amount=params.get("amount")
            )
        else:
            result = {"error": "Unknown trading action"}
        
        return result
    
    async def _handle_image_generation(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com geração de imagens"""
        from ..generators.image_generator import ImageGenerator
        
        generator = ImageGenerator()
        result = await generator.generate_image_async(
            prompt=params.get("prompt"),
            negative_prompt=params.get("negative_prompt"),
            width=params.get("width", 512),
            height=params.get("height", 512),
            steps=params.get("steps", 20),
            guidance_scale=params.get("guidance_scale", 7.5)
        )
        
        return {"success": True, "image_path": result}
    
    async def _handle_youtube_upload(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Lida com uploads para YouTube"""
        from ..integrations.youtube_manager import YouTubeManager
        
        youtube_manager = YouTubeManager()
        result = await youtube_manager.upload_video(
            video_path=params.get("video_path"),
            title=params.get("title"),
            description=params.get("description"),
            tags=params.get("tags"),
            privacy=params.get("privacy", "private")
        )
        
        return result
    
    def get_capabilities(self) -> Dict[str, bool]:
        """Retorna as capacidades disponíveis do agente"""
        return self.capabilities.copy()
    
    def get_status(self) -> Dict[str, Any]:
        """Retorna status atual do agente"""
        return {
            "openai_configured": self.openai_client is not None,
            "capabilities": self.capabilities,
            "version": "1.0.0"
        }
    
    async def analyze_and_execute(self, natural_language_request: str) -> Dict[str, Any]:
        """
        Analisa uma solicitação em linguagem natural e executa a ação apropriada
        
        Args:
            natural_language_request: Solicitação do usuário em linguagem natural
            
        Returns:
            Resultado da análise e execução
        """
        if not self.openai_client:
            return {"error": "OpenAI not configured"}
        
        try:
            # Analisa a intenção do usuário usando GPT
            system_prompt = """
            Você é um agente de IA especializado em analisar solicitações de usuários.
            Identifique o tipo de tarefa e extraia os parâmetros necessários.
            
            Tipos de tarefa disponíveis:
            - code_generation: gerar código
            - telegram_bot: criar/gerenciar bots do Telegram  
            - trading: operações de trading
            - image_generation: gerar imagens
            - youtube_upload: upload de vídeos
            
            Responda APENAS com um JSON válido no formato:
            {
                "task_type": "tipo_da_tarefa",
                "params": {
                    "param1": "valor1",
                    "param2": "valor2"
                }
            }
            """
            
            response = self.openai_client.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": natural_language_request}
                ],
                temperature=0.1
            )
            
            # Parse da resposta
            analysis = response.choices[0].message.content
            import json
            parsed_analysis = json.loads(analysis)
            
            # Executa a tarefa identificada
            result = await self.process_request(
                parsed_analysis["task_type"],
                parsed_analysis["params"]
            )
            
            return {
                "analysis": parsed_analysis,
                "result": result
            }
            
        except Exception as e:
            self.logger.error(f"Error in analyze_and_execute: {str(e)}")
            return {"error": f"Failed to analyze request: {str(e)}"}
