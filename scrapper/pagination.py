import config as settings


def make_start_list(for_task, total_results):

    starts = []

    if for_task == settings.TASKS[1]:
        max_results = settings.MAX_RESULTS_FOR_RESUME
        max_page_results = settings.MAX_RESULTS_PER_RESUME_PAGE

    else:
        max_results = settings.MAX_RESULTS_FOR_JOB
        max_page_results = settings.MAX_RESULTS_PER_JOB_PAGE

    if total_results > max_results:
        total_results = max_results - 1
        print "# {max}+ results found. Fetching first {total} results".format(max=max_results, total=total_results + 1)

    total_pages = (total_results / max_page_results)
    if total_results % max_page_results > 0:
        total_pages += 1

    print "# Total Pages: <{total}>".format(total=total_pages)

    for i in range(0, total_pages):
        starts.append(max_page_results * i)

    return starts