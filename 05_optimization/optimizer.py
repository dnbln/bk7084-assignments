from random import randint
from city import BuildingType, City

from utils import Queue

from typing import Callable



class Optimizer:
    def __init__(self, city):
        """An optimizer that iteratively optimizes a given city grid."""
        self._city = city

    def step(self, print_info=False):
        """Performs a single optimization step.
        
        Score:
            1. Distance from houses to nearest park should be as small as possible.
            2. Distance from houses to nearest highrise and skyscaraper should be as large as possible.
            3. Distance from houses to nearest office should be as small as possible.
            4. Distances from highrises and skyscrappers to offices should be as small as possible.
            5. No two skyscrapers or high rises can be next to each other (1 plot in between diagonally, horizontally and vertically).
            6. Distance from houses to houses should be as small as possible.

        Args:
            print_info (bool):
                Whether to print information about the optimization step.
        """

        def score(city: City, cs: Callable[[float], bool]):
            # No two skyscrapers or high rises can be next to each other (1 plot in between diagonally, horizontally and vertically).
            for row in range(city.rows):
                for col in range(city.cols):
                    building = city.get_building_type(row, col)
                    if building == BuildingType.HIGHRISE or building == BuildingType.SKYSCRAPER:
                        # Check adjacent buildings
                        for dr in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                if dr == 0 and dc == 0:
                                    continue
                                if row + dr < 0 or row + dr >= city.rows or col + dc < 0 or col + dc >= city.cols:
                                    continue

                                b2 = city.get_building_type(row + dr, col + dc)
                                if b2 == BuildingType.HIGHRISE or b2 == BuildingType.SKYSCRAPER:
                                    return -1

          #  No two parks can be next to each other (1 plot in between diagonally, horizontally and vertically).  
            # for row in range(city.rows):
            #     for col in range(city.cols):
            #         building = city.get_building_type(row, col)
            #         if building == BuildingType.PARK:
            #             # Check adjacent buildings
            #             for dr in [-1, 0, 1]:
            #                 for dc in [-1, 0, 1]:
            #                     if dr == 0 and dc == 0:
            #                         continue
            #                     if row + dr < 0 or row + dr >= city.rows or col + dc < 0 or col + dc >= city.cols:
            #                         continue

            #                     b2 = city.get_building_type(row + dr, col + dc)
            #                     if b2 == BuildingType.PARK:
            #                         return -1 

            # distance from houses to nearest park
            score_value = 0
            for row in range(city.rows):
                for col in range(city.cols):
                    building = city.get_building_type(row, col)

                    if building == BuildingType.HOUSE:
                        # Find the nearest park
                        nearest_park_distance = float('inf')

                        q = Queue(1024)
                        q.enqueue((row, col, 0))
                        vis = [False] * (city.rows * city.cols)
                        vis[row * city.cols + col] = True

                        while not q.is_empty():
                            r, c, d = q.dequeue()

                            if r < 0 or r >= city.rows or c < 0 or c >= city.cols:
                                continue

                            if vis[r * city.cols + c]:
                                continue

                            vis[r * city.cols + c] = True

                            if city.get_building_type(r, c) == BuildingType.PARK:
                                nearest_park_distance = d
                                break

                            if r + 1 < city.rows and not vis[(r + 1) * city.cols + c]:
                                q.enqueue((r + 1, c, d + 1))
                            if r - 1 >= 0 and not vis[(r - 1) * city.cols + c]:
                                q.enqueue((r - 1, c, d + 1))
                            if c + 1 < city.cols and not vis[r * city.cols + c + 1]:
                                q.enqueue((r, c + 1, d + 1))
                            if c - 1 >= 0 and not vis[r * city.cols + c - 1]:
                                q.enqueue((r, c - 1, d + 1))

                        # Score based on distance to nearest park
                        score_value += 1 / (nearest_park_distance + 1)

            # Distance from houses to houses should be as small as possible.
            score_value = 0
            for row in range(city.rows):
                for col in range(city.cols):
                    building = city.get_building_type(row, col)

                    if building == BuildingType.HOUSE:
                        # Find the nearest house
                        nearest_house_distance = float('inf')
                        q = Queue(1024)
                        q.enqueue((row-1, col, 1))
                        q.enqueue((row+1, col, 1))
                        q.enqueue((row, col-1, 1))
                        q.enqueue((row, col+1, 1))

                        vis = [False] * (city.rows * city.cols)
                        vis[row * city.cols + col] = True

                        while not q.is_empty():
                            r, c, d = q.dequeue()

                            if r < 0 or r >= city.rows or c < 0 or c >= city.cols:
                                continue
                            
                            if vis[r * city.cols + c]:
                                continue

                            vis[r * city.cols + c] = True

                            if city.get_building_type(r, c) == BuildingType.HOUSE:
                                nearest_house_distance = d
                                break

                            if r + 1 < city.rows and not vis[(r + 1) * city.cols + c]:
                                q.enqueue((r + 1, c, d + 1))
                            if r - 1 >= 0 and not vis[(r - 1) * city.cols + c]:
                                q.enqueue((r - 1, c, d + 1))
                            if c + 1 < city.cols and not vis[r * city.cols + c + 1]:
                                q.enqueue((r, c + 1, d + 1))
                            if c - 1 >= 0 and not vis[r * city.cols + c - 1]:
                                q.enqueue((r, c - 1, d + 1))
                        
                        # Score based on distance to nearest park
                        score_value += 1 / (nearest_house_distance + 1)


            # Distance from houses to nearest highrise and skyscaraper should be as large as possible.
            for row in range(city.rows):
                for col in range(city.cols):
                    building = city.get_building_type(row, col)

                    if building == BuildingType.HOUSE:
                        nearest_highrise_distance = float('inf')

                        q = Queue(1024)
                        q.enqueue((row-1, col, 1))
                        q.enqueue((row+1, col, 1))
                        q.enqueue((row, col-1, 1))
                        q.enqueue((row, col+1, 1))

                        vis = [False] * (city.rows * city.cols)
                        vis[row * city.cols + col] = True

                        while not q.is_empty():
                            r, c, d = q.dequeue()

                            if r < 0 or r >= city.rows or c < 0 or c >= city.cols:
                                continue

                            if vis[r * city.cols + c]:
                                continue

                            vis[r * city.cols + c] = True

                            bt = city.get_building_type(r, c)
                            if bt == BuildingType.SKYSCRAPER or bt == BuildingType.HIGHRISE:
                                nearest_highrise_distance = d
                                break

                            if r + 1 < city.rows and not vis[(r + 1) * city.cols + c]:
                                q.enqueue((r + 1, c, d + 1))
                            if r - 1 >= 0 and not vis[(r - 1) * city.cols + c]:
                                q.enqueue((r - 1, c, d + 1))
                            if c + 1 < city.cols and not vis[r * city.cols + c + 1]:
                                q.enqueue((r, c + 1, d + 1))
                            if c - 1 >= 0 and not vis[r * city.cols + c - 1]:
                                q.enqueue((r, c - 1, d + 1))

                        # Score based on distance to nearest park
                        score_value += nearest_highrise_distance
            
            # Distance from houses to nearest office should be as small as possible.

            offices = []
            for row in range(city.rows):
                for col in range(city.cols):
                    if city.get_building_type(row, col) == BuildingType.OFFICE:
                        offices.append((row, col))

            for row in range(city.rows):
                for col in range(city.cols):
                    building = city.get_building_type(row, col)

                    if building == BuildingType.HOUSE:
                        nearest_office_distance = float('inf')

                        for r, c in offices:
                            distance = abs(row - r) + abs(col - c)
                            nearest_office_distance = min(nearest_office_distance, distance)
                        
                        # Score based on distance to nearest park
                        score_value += 1 / (nearest_office_distance + 1)
            
            # Distances from highrises and skyscrappers to offices should be as small as possible.
            for row in range(city.rows):
                for col in range(city.cols):
                    building = city.get_building_type(row, col)

                    if building == BuildingType.HIGHRISE or building == BuildingType.SKYSCRAPER:
                        total_dist = 0
                        count = len(offices)

                        for r, c in offices:
                            total_dist += abs(row - r) + abs(col - c)

                        score_value += 1 / ((total_dist / count) + 1)
            
            if cs(score_value):
                score_value += sum(1/x for x in city.compute_sunlight_scores())

            return score_value




        #  Hint: You can use the following code to swap two buildings:
        previous_score = score(self._city, lambda _: True)

        row1, col1 = randint(0, self._city._plots_per_row - 1), randint(0, self._city._plots_per_col - 1)
        row2, col2 = randint(0, self._city._plots_per_row - 1), randint(0, self._city._plots_per_col - 1)
        self._city.swap_buildings(row1, col1, row2, col2)
        accepted_swap = True
        #  Hint: You can use the function `compute_sunlight_scores` of the City class
        #  to compute the sunlight scores
        new_score = score(self._city, lambda x: x > previous_score - 20)

        if new_score < previous_score:
            if print_info:
                print("Reverting swap")
            self._city.revert_swap(row1, col1, row2, col2)
            accepted_swap = False

        if print_info:
            print("Previous score: ", previous_score)
            print("New score: ", new_score)
            print("New city layout: ")
            self._city.print_plots()
        
        return new_score, accepted_swap

    def optimize(self, n_steps=100, print_info=False):
        """
        Runs the optimizer for a fixed number of steps.
        Args:
            n_steps (int):
                The number of optimization steps.
            print_info (bool):
                Whether to print information about the optimization step.
        """
        # TODO: Change this method to add a stopping criterion, e.g. stop when
        #  the score does not improve anymore.
        self._city.reset_grid()
        print("Initial scores: ", self._city.compute_sunlight_scores())
        print("Initial scores sum: ", sum(self._city.compute_sunlight_scores()))
        print("Initial city layout: ")
        self._city.print_plots()
        print("Optimizing...")

        denied_swap_count = 0
        for i in range(n_steps):
            print(f"Step: {i}", end="\r")
            score, accepted_swap = self.step(print_info)
            if not accepted_swap:
                denied_swap_count += 1
                if denied_swap_count > 15:
                    break
            else:
                denied_swap_count = 0
        print(f"\nDone! Final score: {score}")
