from pydantic import BaseModel, Field
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    # name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    # power_level: float = Field(ge=0.0, le=100.0)
    # oxygen_level: float = Field(ge=0.0, le=100.0)
    # last_maintenance: datetime = Field(default_factory=datetime.now)
    # is_operational: bool = Field(default=True)
    # notes: str = Field(default="wtf", max_length=200)


valid_object = SpaceStation(station_id="max1", crew_size=5)
print(valid_object)

try:
    invalid_object = SpaceStation(station_id="max1", crew_size=0)
    print(invalid_object)
except Exception as e:
    print(e)
