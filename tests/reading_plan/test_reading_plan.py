from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from tests.assets.news import NEWS
import pytest


def mock_data():
    return NEWS


def test_reading_plan_group_news(mocker):
    mocker.patch('tech_news.analyzer.reading_plan.find_news', mock_data)

    data = ReadingPlanService.group_news_for_available_time(3)

    assert len(data['readable']) == 4
    assert len(data['unreadable']) == 4

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)
