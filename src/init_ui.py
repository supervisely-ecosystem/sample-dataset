
def init_context(data, team_id, workspace_id, project_id):
    data["teamId"] = team_id
    data["workspaceId"] = workspace_id
    data["projectId"] = project_id


def init_options(data, state):
    state['samplePercent'] = 20
    state["dstProjectMode"] = "newProject"
    state["dstProjectName"] = "sample_project"
    state["dstProjectId"] = None

    data["processing"] = False
