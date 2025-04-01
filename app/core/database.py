from typing import AsyncIterator
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from .config import settings


class DatabaseManager:
    def __init__(
        self,
        url: str,
        echo: bool = False,
        pool_size: int = 50,
        max_overflow: int = 10,
        pool_pre_ping: bool = False,
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
            pool_pre_ping=pool_pre_ping,
        )

        self.session_factory = async_sessionmaker(
            bing=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        if self.engine is None:
            raise Exception('DatabaseSessionManager не инициализирован')
        await self.engine.dispose()


database_manager = DatabaseManager(
    url=settings.db.url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
    pool_pre_ping=settings.db.pool_pre_ping,
)


async def get_session() -> AsyncIterator[AsyncSession]:
    async with database_manager.session_factory() as session:
        yield session
