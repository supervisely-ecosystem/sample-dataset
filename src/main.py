
import random
import supervisely as sly
import sly_globals as g
import init_ui


@g.my_app.callback("sample_dataset")
@sly.timeit
def sample_dataset(api: sly.Api, task_id, context, state, app_logger):

    sample_percent = state['samplePercent'] * 0.01
    project_name = state['dstProjectName']
    dst_project_id = state["dstProjectId"]

    if dst_project_id is None:
        dst_project = api.project.create(g.WORKSPACE_ID, project_name, change_name_if_conflict=True)
        dst_project_id = dst_project.id

    api.project.merge_metas(g.PROJECT_ID, dst_project_id)

    datasets = api.dataset.get_list(g.PROJECT_ID)
    progress_items_cb = init_ui.get_progress_cb(api, task_id, 1, "Finished", len(datasets))
    for scr_dataset in datasets:

        image_infos = api.image.get_list(scr_dataset.id)
        image_ids = [image_info.id for image_info in image_infos]

        sample_choose = round(len(image_ids) * sample_percent)
        sample_ids = random.sample(image_ids, sample_choose)

        curr_dst_ds = api.dataset.create(dst_project_id, scr_dataset.name, change_name_if_conflict=True)
        for sample_batch in sly.batched(sample_ids):
            api.image.copy_batch(curr_dst_ds.id, sample_batch, with_annotations=True)

        progress_items_cb(1)

    init_ui.reset_progress(api, task_id, 1)

    api.app.set_field(task_id, "data.processing", False)
    api.task.set_output_project(task_id, dst_project_id, project_name)

    #g.my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": g.TEAM_ID,
        "WORKSPACE_ID": g.WORKSPACE_ID,
        "PROJECT_ID": g.PROJECT_ID
    })

    data = {}
    state = {}

    init_ui.init_context(data, g.TEAM_ID, g.WORKSPACE_ID, g.PROJECT_ID)
    init_ui.init_options(data, state)
    init_ui.init_progress(data, state)

    g.my_app.compile_template(g.root_source_dir)
    g.my_app.run(data=data, state=state)


if __name__ == '__main__':
    sly.main_wrapper("main", main)