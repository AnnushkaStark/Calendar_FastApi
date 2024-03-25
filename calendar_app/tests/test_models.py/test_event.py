from sqlalchemy.ext.asyncio import AsyncSession

from calendar_app.models.event_model import Event


class TestEventModel:
    """
    Тест временной
    таблицы event
    на соответствие схеме
    в базе данных
    """
    def jest_fields(
        self,
        async_session: AsyncSession,
    ) -> None:
        current_fields_name = [i for i in Event.__table__.columns]
        related_fields = [i._dependency_processor.key for i in Event.__mapper__.relationships]
        all_model_fields = current_fields_name + related_fields
        schema_fields_name = {
            "title",
            "event_type",
            "priority",
            "repeatability",
            "event_location",
            "organizer",
            "updated_at",
            "start_time",
            "end_time",
            "duration",
            "description",
            "owner_id",
            "is_active",
            "participants",
        }
        for field in schema_fields_name:
            assert field in all_model_fields, "Нет необходимого поля %s" % field
