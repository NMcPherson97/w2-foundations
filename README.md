### Skills ###
Skills are prompts and task descriptions that are saved in skill folders attached to the agent's harness/workspace. This provides the user a short-hand method of telling the agent what to do, eliminating repetition and reducing inconsistent responses or behavior from the agent. 

### Hooks ###
Hooks are automated scripts that run at a specified point in the agent loop. They can be used to allow, block, or modify inputs from the agent.

### Permissions ###
Permissions are instructions for how an agent handles sensitive actions:
Allow runs without an extra prompt
Ask pauses for your approval
Deny blocks the action
In the absence of explicit instructions from a user, the agent will always Deny first, then Ask. 