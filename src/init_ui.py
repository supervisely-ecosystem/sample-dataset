
import supervisely as sly
from functools import partial


def init_context(data, team_id, workspace_id, project_id):
    data["teamId"] = team_id
    data["workspaceId"] = workspace_id
    data["projectId"] = project_id


def init_options(data, state):
    state['samplePercent'] = 20
    state["dstProjectMode"] = "newProject"
    state["dstProjectName"] = "sample_project"
    state["dstProjectId"] = None
    data["srcProjectName"] = None

    data["processing"] = False


def init_progress(data, state):
    data["progressName1"] = None
    data["currentProgressLabel1"] = 0
    data["totalProgressLabel1"] = 0
    data["currentProgress1"] = 0
    data["totalProgress1"] = 0


def _set_progress(index, api, task_id, message, current_label, total_label, current, total):
    fields = [
        {"field": f"data.progressName{index}", "payload": message},
        {"field": f"data.currentProgressLabel{index}", "payload": current_label},
        {"field": f"data.totalProgressLabel{index}", "payload": total_label},
        {"field": f"data.currentProgress{index}", "payload": current},
        {"field": f"data.totalProgress{index}", "payload": total},
    ]
    api.task.set_fields(task_id, fields)


def _update_progress_ui(api, task_id, progress: sly.Progress, index):
    _set_progress(index, api, task_id, progress.message, progress.current_label, progress.total_label, progress.current, progress.total)


def update_progress(count, index, api: sly.Api, task_id, progress: sly.Progress):
    count = min(count, progress.total - progress.current)
    progress.iters_done(count)
    if progress.need_report():
        progress.report_progress()
        _update_progress_ui(api, task_id, progress, index)


def get_progress_cb(api, task_id, index, message, total, is_size=False, func=update_progress):
    progress = sly.Progress(message, total, is_size=is_size)
    progress_cb = partial(func, index=index, api=api, task_id=task_id, progress=progress)
    progress_cb(0)
    return progress_cb


def reset_progress(api, task_id, index):
    _set_progress(index, api, task_id, None, 0, 0, 0, 0)


def init_project_fields(api, task_id, src_project):
    fields = [
        {"field": "data.srcProjectType", "payload": src_project.type},
        {"field": "data.srcProjectName", "payload": src_project.name},
        {"field": "data.projectId", "payload": src_project.id},
        {"field": "data.srcProjectPreviewUrl", "payload": api.image.preview_url(src_project.reference_image_url,
                                                                                      100, 100)},
        {"field": "data.finished", "payload": False}
    ]
    api.app.set_fields(task_id, fields)
