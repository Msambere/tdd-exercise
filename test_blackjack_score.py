from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]

  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score ==7

#@pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  hand = [5, "Jack"]
  score = blackjack_score(hand)

  assert score == 15

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = ["Ace", 10]  
  score = blackjack_score(hand)

  assert score == 21

# @pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  hand = ["Ace", "Ace", 8]  
  score = blackjack_score(hand)

  assert score == 20

#@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  assert blackjack_score([11,"Jack"])== "Invalid"
  assert blackjack_score(["two", "eight"]) == "Invalid"


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  assert blackjack_score([2,2,2,4,3,2]) == "Invalid"

# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  assert blackjack_score(["Jack", "Queen", 5]) == "Bust"


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  assert blackjack_score(["Ace","Ace", "King"])== 12

# @pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
  assert blackjack_score(["Ace","Ace", "Ace", "Ace"])== 14
    