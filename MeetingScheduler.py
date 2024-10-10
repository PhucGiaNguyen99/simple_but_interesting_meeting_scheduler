from Meeting import Meeting


class MeetingScheduler:
    """Handles scheduling, sorting, and management of meetings."""

    def __init__(self):
        self._meetings = []

    def add_meeting(self, meeting):
        """Add a new meeting and sort the list using a custom insertion sort algorithm."""
        self._meetings.append(meeting)
        self.insertion_sort_meetings()

    def insertion_sort_meetings(self):
        """Sort the meetings using insertion sort based on their date."""
        for i in range(len(self._meetings)):
            key = self._meetings[i]
            j = i - 1
            # Consider the range [0, ...i]
            # Move elements that are greater than key, to one position ahead
            while j >= 0 and key < self._meetings[j]:
                self._meetings[j + 1] = self._meetings[j]
                j -= 1
            self._meetings[j + 1] = key
