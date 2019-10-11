TODO:
- train interactive

--

# Rasa Recruiting Bot

This repo contains a Rasa bot that greets applicants, checks which
positions are open, and checks the status of their application.

## Usage

```
rasa train
rasa shell
```

## Open Positions

If the user says something like "what positions are open", the
bot will follow up by asking whether they are looking for a technical
or a business role. This is implemented as an utterance with a template
defined in `domain.yml`, and a categorical slot named "role_type" whose value
can be one of "technical", "business", or "any". However, if the user says
something like "what technical positions are open", the "role_type" slot is
filled directly and no follow-up is required.

In either cas, the `ActionCheckPositions` class then gets the appropriate
positions and fills the "positions" slot. Then, the `ActionUtterPositions`
class formats the result depending on the number of positions available, and
responds to the user.

## Application Status

Checking the status of an application is implemented with four separate
stories and corresponding utterances, one for each possible status (received,
rejected, interview, or unknown). Although it is possible to implement this
with a single story and an action that formats the response, this design
did not result in enough training data for the bot to be reliable.

Checking the status of an application requires that the user provide their
name. This is handled by the `ApplicationStatusForm`, which has `PERSON` as
a required slot.  This slot can get filled either by the corresponding `PERSON`
entity populated by the `SpacyEntityExtractor` (specified in the pipeline in
`config.yml`), or by whatever text the user responds with when the bot asks
them for their name. This allows the user to specify their name upon greeting
the bot, and not have the bot ask them again when they check for their status.
For example:

```
Your input ->  hi my name is Richard Abrich
hi, I’m Rasa’s recruiting bot. How can I help?
Your input ->  what is the status of my application
Hi Richard! Let me check that for you
Your status is unknown, please contact support.
```

The `ApplicationStatusForm` responds with an utterance containing the user's
first name only. In addition, it takes an optional `forgetful` parameter which,
if True, clears the `PERSON` slot after it's been submitted, forcing the user
to specify their name each time they want to check the status of an
application.

For example:

#### `forgetful == True`:

```
Your input ->  what is the status of my application
What is your name?
Your input ->  richard abrich
Hi Richard! Let me check that for you
Unfortunately, your application has been rejected.
Your input ->  what is the status of my application
What is your name?
Your input ->  ali park
Hi Ali! Let me check that for you
Unfortunately, your application has been rejected.
```

#### `forgetful == False`:

```
Your input ->  what is the status of my application?
What is your name?
Your input ->  richard abrich
Hi Richard! Let me check that for you
Congratulations, you have an interview!
Your input ->  what is the status of my application?
Hi Richard! Let me check that for you
Congratulations, you have an interview!
```

In both cases, the user can specify any name and ask for the status in a single
turn:

```
Your input ->  my name is Richard Abrich. what is the status of my application?
Hi Richard! Let me check that for you
Unfortunately, your application has been rejected.
Your input ->  my name is Ali Park. what is the status of my application?
Hi Ali! Let me check that for you
Your status is unknown, please contact support.
```

## Tests

Some end to end stories are included in `e2e_stories.md`. To test, run:

```
rasa test --stories e2e_stories.md --e2e
cat results/failed_stories.md
```
