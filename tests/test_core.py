import unittest
from dockerscope import summarize

class DockerScopeTests(unittest.TestCase):
    def test_summary(self): self.assertEqual(summarize([{"status":"running"},{"status":"running"},{"status":"exited"}]), {"exited":1,"running":2})

if __name__ == "__main__": unittest.main()
