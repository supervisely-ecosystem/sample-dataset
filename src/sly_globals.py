
import os
import supervisely as sly

my_app = sly.AppService()
api: sly.Api = my_app.public_api

TASK_ID = int(os.environ["TASK_ID"])
TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
PROJECT_ID = int(os.environ['modal.state.slyProjectId'])

sample_percent = int(os.environ['modal.state.samplePercent'])
