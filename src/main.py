
import os
import supervisely as sly
import sly_globals as g


@g.my_app.callback("sample_dataset")
@sly.timeit
def sample_dataset(api: sly.Api, task_id, context, state, app_logger):

    project = api.project.get_info_by_id(g.PROJECT_ID)
    meta_json = api.project.get_meta(g.PROJECT_ID)
    meta = sly.ProjectMeta.from_json(meta_json)




    # splitted_project_name = project.name + g.new_project_suffix
    # new_project = api.project.create(g.WORKSPACE_ID, splitted_project_name, type=sly.ProjectType.VIDEOS,
    #                                   change_name_if_conflict=True)
    # api.project.update_meta(new_project.id, meta.to_json())
    # meta_json = api.project.get_meta(g.PROJECT_ID)
    # meta = sly.ProjectMeta.from_json(meta_json)
    #
    # result_dir = os.path.join(g.my_app.data_dir, g.result_dir_name)
    # for dataset in api.dataset.get_list(g.PROJECT_ID):
    #     ds = api.dataset.create(new_project.id, dataset.name, change_name_if_conflict=True)
    #     videos = api.video.get_list(dataset.id)
    #     progress = sly.Progress('Video being splitted', len(videos))
    #     for video_info in videos:
    #         ann_info = api.video.annotation.download(video_info.id)
    #         ann = sly.VideoAnnotation.from_json(ann_info, meta, g.key_id_map)
    #         video_length = video_info.frames_to_timecodes[-1]
    #
    #         if g.split_frames:
    #             if g.split_frames >= len(video_info.frames_to_timecodes):
    #                 g.logger.warn('Frames count, set for splitting, is more then video {} length'.format(video_info.name))
    #                 upload_full_video(api, ds.id, video_info, ann, progress)
    #                 continue
    #             splitter = get_frames_splitter(g.split_frames, video_info.frames_to_timecodes)
    #
    #         if g.split_sec:
    #             if g.split_sec >= round(video_length):
    #                 g.logger.warn('Time, set for splitting, is more then video {} length'.format(video_info.name))
    #                 upload_full_video(api, ds.id, video_info, ann, progress)
    #                 continue
    #             splitter = get_time_splitter(g.split_sec, video_length)
    #
    #         curr_video_paths, curr_video_names = write_videos(api, splitter, result_dir, video_info)
    #         new_video_infos = api.video.upload_paths(ds.id, curr_video_names, curr_video_paths)
    #         upload_new_anns(api, new_video_infos, ann)
    #         progress.iter_done_report()

    g.my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "TEAM_ID": g.TEAM_ID,
        "WORKSPACE_ID": g.WORKSPACE_ID,
        "modal.state.slyProjectId": g.PROJECT_ID
    })

    data = {"workspaceId": g.WORKSPACE_ID}
    state = {}


    g.my_app.run(data=data, initial_events=[{"command": "sample_dataset"}])


if __name__ == '__main__':
    sly.main_wrapper("main", main)