
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st = deque(students)
        sn = deque(sandwiches)

        rotations = 0

        while st and rotations != len(st):
            if st[0] == sn[0]:
                st.popleft()
                sn.popleft()
                rotations = 0
            else:
                st.append(st.popleft())
                rotations += 1
            


        return len(st)
