## greet
* greet
  - utter_greet

## positions open now
* positions_open_now
  - utter_technical_or_business
* inform
  - action_check_positions
  - action_utter_positions

## positions open now -- business
* positions_open_now{"role_type": "business"}
    - slot{"role_type": "business"}
    - action_check_positions
    - action_utter_positions

## positions open now -- technical
* positions_open_now{"role_type": "technical"}
    - slot{"role_type": "technical"}
    - action_check_positions
    - action_utter_positions

## application status received
* application_status
  - application_status_form
  - action_check_status
  - slot{"status": "received"}
  - utter_status_received
## application status rejected
* application_status
  - application_status_form
  - action_check_status
  - slot{"status": "rejected"}
  - utter_status_rejected
## application status interview
* application_status
  - application_status_form
  - action_check_status
  - slot{"status": "interview"}
  - utter_status_interview
## application status unknown
* application_status
  - application_status_form
  - action_check_status
  - slot{"status": "unknown"}
  - utter_status_unknown
