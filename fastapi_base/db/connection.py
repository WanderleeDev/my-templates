from src.common import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


url, driver = settings.DATABASE_URL, settings.DATABASE_DRIVER
i = url.index(":")
DATABASE_URI = (
    f"{settings.DATABASE_URL[:i]}+{settings.DATABASE_DRIVER}{settings.DATABASE_URL[i:]}"
)

engine = create_async_engine(url=DATABASE_URI, echo=True)
async_session = async_sessionmaker(bind=engine, class_=AsyncSession)
