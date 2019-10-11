## end-to-end story: positions
* greet: hi
   - utter_greet
* positions_open_now: I’d like to know which positions are open right now
   - utter_technical_or_business
* inform: A [technical](role_type) one
   - action_check_positions
   - action_utter_positions

## end-to-end story: positions with role_type
* positions_open_now: I’d like to know which [business](role_type) positions are open right now
   - action_check_positions
   - action_utter_positions

# end-to-end story: status received
* application_status: Hi, my name is [Ali Park](PERSON). I applied for a job and would like to know when I’ll hear back
   - slot{"PERSON": "Ali Park"}
   - application_status_form
   - action_check_status
   - slot{"status": "received"}
   - utter_status_received

# end-to-end story: status rejected
* application_status: Hi, my name is [Ali Park](PERSON). I applied for a job and would like to know when I’ll hear back
   - slot{"PERSON": "Ali Park"}
   - application_status_form
   - action_check_status
   - slot{"status": "rejected"}
   - utter_status_rejected

# end-to-end story: status interview
* application_status: Hi, my name is [Ali Park](PERSON). I applied for a job and would like to know when I’ll hear back
   - slot{"PERSON": "Ali Park"}
   - application_status_form
   - action_check_status
   - slot{"status": "interview"}
   - utter_status_interview

# end-to-end story: status unknown
* application_status: Hi, my name is [Ali Park](PERSON). I applied for a job and would like to know when I’ll hear back
   - slot{"PERSON": "Ali Park"}
   - application_status_form
   - action_check_status
   - slot{"status": "unknown"}
   - utter_status_unknown
