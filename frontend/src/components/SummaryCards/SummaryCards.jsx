import SummaryCard from "../SummaryCard/SummaryCard";

function SummaryCards({ summary, repository }) {
  return (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mt-10">

      <SummaryCard
        title="Python Files"
        value={repository.python_files}
      />

      <SummaryCard
        title="Entities"
        value={summary.entities}
      />

      <SummaryCard
        title="Issues"
        value={summary.issues}
      />

      <SummaryCard
        title="High Priority"
        value={summary.high_priority_items}
      />

    </div>
  );
}

export default SummaryCards;