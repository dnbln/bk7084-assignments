from random import randint
from city import BuildingType


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

            Neighborhood and Zoning Rules
                Mixed Zoning Bonus:

                    Reward layouts where neighborhoods have a balanced mix of building types (e.g., houses, offices, parks, and flexible plots).
                    Penalize over-concentration of any one building type within a defined radius (e.g., 5x5 grid).
            
                Cultural or Commercial Centers:

                    Bonus for clustering offices and skyscrapers together in designated areas (e.g., a "business district") while keeping houses and parks further away.
                
                Low-Density Buffer Zones:

                    Score higher if low-density buildings (houses and parks) are used as buffers around high-density buildings (skyscrapers and high-rises).
            
            
            Traffic and Connectivity Rules
                Accessibility to Roads:

                    Reward layouts where offices, houses, and skyscrapers are near major roads or pathways (assumed to be part of your city grid).
                Commute Optimization:

                    Penalize houses that are too far from offices or are "isolated" (e.g., not within a certain radius of any other houses).
                Walkability:

                    Score higher for designs where residents can access parks and offices within a walkable distance (e.g., 1-2 plots).
            
            
            Environmental and Aesthetic Rules
                Green Space Integration:

                    Parks surrounded by high-rises or skyscrapers receive penalties unless adequately spaced.
                    Score higher for "central park" designs where parks are surrounded by houses or mixed-use buildings.
                Natural Light Cascading:

            Assign bonuses for configurations where sunlight "cascades" down building heights, with shorter buildings in the shadow of taller ones.
            View Optimization:

            Score higher for houses that have an unobstructed view of parks or open spaces.
            Resource Distribution Rules
            Equitable Distribution:

            Ensure each quadrant of the grid has proportional amounts of parks, offices, and flexible plots.
            Penalize layouts that overly favor one region (e.g., all skyscrapers in one corner).
            Proximity to Amenities:

            Additional scoring for houses near two or more amenities (e.g., park + office or park + high-rise).
            Advanced Sunlight and Shadow Rules
            Seasonal Sunlight Scoring:

            Adjust sunlight scoring to account for different angles throughout the year. Favor houses and parks that receive consistent sunlight across all seasons.
            Shadow Management:

            Assign penalties for skyscrapers and high-rises that cast large shadows on other tall buildings (e.g., a high-rise shadowing another high-rise).
            Economic and Social Rules
            Economic Hubs:

            Score higher if offices and skyscrapers are closer to each other, promoting commercial hubs.
            Social Interaction Zones:

            Parks near clusters of houses receive bonuses for fostering community interaction.
            Dynamic Interaction Rules
            Sunlight-Driven Placement:

            Favor placement of skyscrapers on the north side of parks and houses, leaving the south side open to maximize sunlight.
            Noise Pollution:

            Penalize layouts where noisy buildings (e.g., offices, high-rises, skyscrapers) are directly adjacent to houses.
            Bonus Criteria
            Aesthetic Cohesion:

            Reward clusters of buildings with a visually pleasing arrangement, such as alternating patterns or symmetry.
            Energy Efficiency:

            Score higher for compact layouts that minimize commuting distances and encourage shared utilities.
            Cultural Significance:

            Create designated areas for cultural landmarks (e.g., special flexible plots near parks or houses).


        Args:
            print_info (bool):
                Whether to print information about the optimization step.
        """

        def score(city):
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


            # distance from houses to nearest park
            score_value = 0
            for row in range(city.rows):
                for col in range(city.cols):
                    building = city.get_building_type(row, col)

                    if building == BuildingType.HOUSE:
                        # Find the nearest park
                        nearest_park_distance = float('inf')
                        for r in range(city.rows):
                            for c in range(city.cols):
                                if city.get_building_type(r, c) == BuildingType.PARK:
                                    distance = abs(row - r) + abs(col - c)
                                    nearest_park_distance = min(nearest_park_distance, distance)
                        
                        # Score based on distance to nearest park
                        score_value += 1 / (nearest_park_distance + 1)
            
            # Distance from houses to nearest highrise and skyscaraper should be as large as possible.
            for row in range(city.rows):
                for col in range(city.cols):
                    building = city.get_building_type(row, col)

                    if building == BuildingType.HOUSE:
                        nearest_highrise_distance = float('inf')

                        for r in range(city.rows):
                            for c in range(city.cols):
                                if city.get_building_type(r, c) == BuildingType.HIGHRISE or city.get_building_type(r, c) == BuildingType.SKYSCRAPER:
                                    distance = abs(row - r) + abs(col - c)
                                    nearest_highrise_distance = min(nearest_highrise_distance, distance)
                        
                        # Score based on distance to nearest park
                        score_value += nearest_highrise_distance
            
            # Distance from houses to nearest office should be as small as possible.

            for row in range(city.rows):
                for col in range(city.cols):
                    building = city.get_building_type(row, col)

                    if building == BuildingType.HOUSE:
                        nearest_office_distance = float('inf')

                        for r in range(city.rows):
                            for c in range(city.cols):
                                if city.get_building_type(r, c) == BuildingType.OFFICE:
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
                        count = 0

                        for r in range(city.rows):
                            for c in range(city.cols):
                                if city.get_building_type(r, c) == BuildingType.OFFICE:
                                    distance = abs(row - r) + abs(col - c)
                                    total_dist += distance
                                    count += 1
                        
                        # Score based on distance to nearest park
                        if count == 0:
                            continue

                        score_value += 1 / ((total_dist / count) + 1)
            
            score_value += sum(city.compute_sunlight_scores())
            return score_value




        # TODO: Implement your optimization algorithm here.
        #  Hint: You can use the following code to swap two buildings:
        previous_score = score(self._city)

        row1, col1 = randint(0, self._city._plots_per_row - 1), randint(0, self._city._plots_per_col - 1)
        row2, col2 = randint(0, self._city._plots_per_row - 1), randint(0, self._city._plots_per_col - 1)
        self._city.swap_buildings(row1, col1, row2, col2)
        #  Hint: You can use the function `compute_sunlight_scores` of the City class
        #  to compute the sunlight scores
        new_score = score(self._city)

        if new_score < previous_score:
            if print_info:
                print("Reverting swap")
            self._city.swap_buildings(row1, col1, row2, col2)

        if print_info:
            print("Previous score: ", previous_score)
            print("New score: ", new_score)
            print("New city layout: ")
            self._city.print_plots()
        
        return new_score

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
        for i in range(n_steps):
            print(f"Step: {i}", end="\r")
            score = self.step(print_info)
            # TODO: Add a stopping criterion here.
        print(f"\nDone! Final score: {score}")