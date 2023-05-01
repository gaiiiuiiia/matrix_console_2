import pytest

from src.utils import Boundary, Position, get_random_position_in_boundary, reverse_median


class TestBoundary:

    @pytest.fixture
    def boundaries(self) -> list[Boundary]:
        p1 = Position(0, 0)
        p2 = Position(5, 5)
        return [Boundary(p1, p2), Boundary(p2, p1)]

    @pytest.fixture
    def positions_in_boundary(self) -> list[Position]:
        return [
            Position(0, 0),
            Position(2, 3),
            Position(5, 5),
            Position(0, 5),
            Position(5, 0),
        ]

    @pytest.fixture
    def positions_out_of_boundary(self) -> list[Position]:
        return [
            Position(-1, -1),
            Position(6, 6),
            Position(5, 6),
            Position(0, -2),
        ]

    def test_position_in_boundary(self, positions_in_boundary, boundaries) -> None:
        for boundary in boundaries:
            for position in positions_in_boundary:
                assert position in boundary

    def test_position_not_in_boundary(self, positions_out_of_boundary, boundaries) -> None:
        for boundary in boundaries:
            for position in positions_out_of_boundary:
                assert position not in boundary

    def test_boundary_repr(self) -> None:
        boundary = Boundary(Position(0, 0), Position(1, 2))
        assert repr(boundary) == 'Boundary(Position(0, 0), Position(1, 2))'


def test_get_random_position_in_boundary() -> None:
    boundary = Boundary(Position(0, 0), Position(5, 5))
    position = get_random_position_in_boundary(boundary)

    assert position in boundary


@pytest.mark.parametrize(
    ['bounds', 'val', 'reversed_val'],
    [
        ((1, 10), 1, 10),
        ((1, 10), 10, 1),
        ((1, 10), 5, 6),
        ((1, 10), 6, 5),
        ((1, 3), 1, 3),
        ((1, 3), 3, 1),
        ((1, 3), 2, 2),
    ]
)
def test_reverse_median(bounds, val, reversed_val) -> None:
    assert reverse_median(val, *bounds) == reversed_val
