
import os
import supervisely as sly

my_app = sly.AppService()
api: sly.Api = my_app.public_api

TASK_ID = int(os.environ["TASK_ID"])
TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
PROJECT_ID = int(os.environ['context.slyProjectId'])
DATASET_ID = int(os.environ['context.slyDatasetId'])

sample_percent = int(os.environ['gui.state.samplePercent'])
save_mode = os.environ['gui.state.dstProjectMode']
