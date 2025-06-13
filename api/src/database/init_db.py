import logging

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from src.config.settings import get_settings

logger = logging.getLogger(__name__)

settings = get_settings()


class MongoDB:
    _client: AsyncIOMotorClient | None = None
    _db: AsyncIOMotorDatabase | None = None

    @classmethod
    async def initialize_db(cls):
        if cls._client is None:
            logger.info(f"Initializing MongoDB client with URL: {settings.mongodb_url}")
            try:
                cls._client = AsyncIOMotorClient(settings.mongodb_url)
                await cls._client.admin.command("ping")
                print("✅✅ Ping Successful")
            except Exception as e:
                logger.error(f"Error initializing MongoDB client: {e}")

        if cls._client and cls._db is None:
            logger.info(f"Using database: {settings.mongodb_db_name}")
            cls._db = cls._client[settings.mongodb_db_name]
            logger.info(f"Connected to MongoDB database: {settings.mongodb_db_name}")

    @classmethod
    async def get_db(cls) -> AsyncIOMotorDatabase:
        if cls._db is None:
            await cls.initialize_db()
            logger.info(f"Using database: {settings.mongodb_db_name}")
        return cls._db

    @classmethod
    async def close(cls):
        if cls._client:
            cls._client.close()
            cls._client = None
            cls._db = None
            logger.info("MongoDB client closed")
