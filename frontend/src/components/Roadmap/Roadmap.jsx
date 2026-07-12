import RoadmapCard from "../RoadmapCard/RoadmapCard";

function Roadmap({ roadmap }) {
  return (
    <div className="mt-12">

      <h2 className="text-3xl font-bold mb-6">
        Top Refactoring Roadmap
      </h2>

      <div className="space-y-6">

        {roadmap.map((item) => (

          <RoadmapCard
            key={item.rank}
            item={item}
          />

        ))}

      </div>

    </div>
  );
}

export default Roadmap;