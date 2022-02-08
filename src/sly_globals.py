
import os, sys
from pathlib import Path
import supervisely as sly

my_app = sly.AppService()
api: sly.Api = my_app.public_api

root_source_dir = str(Path(sys.argv[0]).parents[1])
sly.logger.info(f"Root source directory: {root_source_dir}")
sys.path.append(root_source_dir)

TASK_ID = int(os.environ["TASK_ID"])
TEAM_ID = int(os.environ['context.teamId'])
WORKSPACE_ID = int(os.environ['context.workspaceId'])
PROJECT_ID = int(os.environ['context.projectId'])

# sample_percent = int(os.environ['gui.state.samplePercent'])
# save_mode = os.environ['gui.state.dstProjectMode']
