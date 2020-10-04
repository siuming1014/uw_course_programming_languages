# python3
import heapq


class JobQueue:
    def __init__(self):
        self.num_workers = None
        self.jobs = None
        self.assigned_workers = []
        self.start_times = []

        self.workers_jobs = []

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        self.workers_jobs = [(0, i) for i in range(self.num_workers)]
        heapq.heapify(self.workers_jobs)
        for i in range(len(self.jobs)):
            time, worker = self.workers_jobs[0]
            self.assigned_workers.append(worker)
            self.start_times.append(time)
            heapq.heapreplace(self.workers_jobs, (time + self.jobs[i], worker))

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

