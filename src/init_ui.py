
def init_context(data, team_id, workspace_id):
    data["teamId"] = team_id
    data["workspaceId"] = workspace_id

def init(data, state):
    state['samplePercent'] = 20
    state['dstProjectMode'] = 'existingProject'
