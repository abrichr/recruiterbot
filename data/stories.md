## positions open now -- technical
* greet
  - utter_greet
* positions_open_now
  - utter_technical_or_business
* inform
  - action_check_positions
  - action_utter_positions

## when hear back
* application_status
  - application_status_form
  - action_check_status
  - slot{"status": "received"}
  - utter_status_received
## when hear back
* application_status
  - application_status_form
  - action_check_status
  - slot{"status": "rejected"}
  - utter_status_rejected
## when hear back
* application_status
  - application_status_form
  - action_check_status
  - slot{"status": "interview"}
  - utter_status_interview
## when hear back
* application_status
  - application_status_form
  - action_check_status
  - slot{"status": "unknown"}
  - utter_status_unknown
