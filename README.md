# project2
EC601 YongxinJiang   Automated refueling planning process


1.program statement
The program is meticulously designed to ensure that drivers can automatically plan their refueling paths, making the entire driving experience more convenient and efficient.


 
2.User Story
As a driver, your expectation from this program is twofold. For longer journeys, you want the navigation to be intelligent enough to arrange refueling stops strategically along your path. It should consider the total distance to be covered and the vehicle’s fuel efficiency to pinpoint the optimal locations for refueling. The goal is to eliminate the worry of running out of gasoline mid-journey and ensuring that each stop is well-planned and doesn’t lead to unnecessary detours.
In the case of shorter trips, the program should aim at identifying a refueling station near the destination point. This ensures that upon arrival, the vehicle is refueled and ready for the next journey. It’s about instilling confidence in the driver that they won’t be left stranded due to an empty fuel tank and that the next trip can be started without any trouble.


 
3.MVPS
For the MVP, the process begins with the program retrieving the path between the designated starting point and the end point. The initial step is to calculate the total distance of the journey. If this distance falls below a certain threshold, the program jumps into action, retrieving all the available gas stations in proximity to the end point. It then selects the closest station, integrates it into the planned path, and re-calculates the journey ensuring the added stop is efficient and doesn’t lead to significant deviations.
For journeys that exceed the predetermined distance threshold, the program adopts a more complex approach. It doesn’t just look at the end point but also keeps an eye on the entire path. At regular intervals, based on the vehicle’s fuel consumption rate and the total distance to be covered, it identifies potential refueling points. It retrieves the gas stations available surrounding these points, evaluates them based on proximity and convenience, and then seamlessly integrates the selected stations into the path. The re-planned path ensures that the driver can cover the long distance with confidence, knowing well that refueling stops have been systematically arranged.
In essence, this program is about blending technology with foresight. It’s about ensuring that every journey, short or long, is covered with the assurance that refueling won’t be a trouble but a well-orchestrated stop that is woven seamlessly into the journey.
