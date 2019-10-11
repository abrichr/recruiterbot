## end-to-end story: positions
* greet: hello
   - utter_greet
* inform: what positions are open
   - utter_technical_or_business
* inform: [technical](role_type)
   - action_utter_positions

# end-to-end story: status
* inform: my name is Richard Abrich. what is the status of my application?
   - action_check_status
   - slot{"status": "received"}
   - utter_status_received

# end-to-end story: status
* inform: what is the status of my application?
   - application_status_form
* inform: richard abrich
   - action_check_status
   - slot{"status": "interview"}
   - utter_status_interview
