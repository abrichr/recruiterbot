## positions open now -- technical
* greet
  - utter_greet
* positions_open_now
  - utter_technical_or_business
* inform{"role_type": "technical"}
  - action_check_positions
  - action_utter_positions

## positions open now -- business
* greet
  - utter_greet
* positions_open_now
  - utter_technical_or_business
* inform{"role_type": "business"}
  - action_check_positions
  - action_utter_positions

## hear back -- received
* when_hear_back{"name": "Ali"}
  - slot{"name": "Ali"}
  - utter_checking
  - action_check_status
  - slot{"status": "received"}
  - utter_status_received

## hear back -- rejected
* when_hear_back{"name": "Ali"}
  - slot{"name": "Ali"}
  - utter_checking
  - action_check_status
  - slot{"status": "rejected"}
  - utter_status_rejected

## hear back -- interview
* when_hear_back{"name": "Ali"}
  - slot{"name": "Ali"}
  - utter_checking
  - action_check_status
  - slot{"status": "interview"}
  - utter_status_interview

## hear back -- unknown
* when_hear_back{"name": "Ali"}
  - slot{"name": "Ali"}
  - utter_checking
  - action_check_status
  - slot{"status": "unknown"}
  - utter_status_unknown
