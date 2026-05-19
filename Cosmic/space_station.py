from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)

    crew_size: int = Field(ge=1, le=20)

    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)

    last_maintenance: datetime = Field(
        default_factory=datetime.now
    )

    is_operational: bool = True

    notes: Optional[str] = Field(
        default=None,
        max_length=200
    )


def display_station(station: SpaceStation) -> None:
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(
        f"Status: "
        f"{'Operational' if station.is_operational else 'Offline'}"
    )
    print(f"Last Maintenance: {station.last_maintenance}")

    if station.notes:
        print(f"Notes: {station.notes}")


def test_valid_station() -> None:
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
    )

    print("Valid station created:")
    display_station(station)


def test_invalid_crew_size() -> None:
    try:
        SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
        )

    except ValidationError as error:
        print(error.errors()[0]["msg"])


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    test_valid_station()

    print("\n" + "=" * 40)

    print("Expected validation error:")
    test_invalid_crew_size()


if __name__ == "__main__":
    main()
