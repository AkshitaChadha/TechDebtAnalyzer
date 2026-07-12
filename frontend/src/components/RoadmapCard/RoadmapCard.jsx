import ProgressBar from "../ProgressBar/ProgressBar";
function getRank(rank) {
  if (rank === 1) return "🥇";
  if (rank === 2) return "🥈";
  if (rank === 3) return "🥉";

  return `#${rank}`;
}

function RoadmapCard({ item }) {
  return (
    <div
      className={`bg-white rounded-xl shadow-md border-l-8 p-6 transition duration-300 hover:shadow-2xl hover:-translate-y-1 ${
        item.total_score >= 20
          ? "border-red-500"
          : item.total_score >= 10
          ? "border-orange-400"
          : "border-green-500"
      }`}
    >
      <div className="flex justify-between items-start">
        <div>
          <h2 className="text-2xl font-bold flex items-center gap-2">
            <span>{getRank(item.rank)}</span>
            {item.entity}
          </h2>

          <span className="inline-block mt-2 px-3 py-1 rounded-full bg-slate-100 text-slate-600 text-sm">
            {item.entity_type}
          </span>

          <p className="text-sm text-gray-400 mt-3">
            📄 {item.file}
          </p>

          <p className="text-sm text-gray-400">
            Lines {item.start_line} – {item.end_line}
          </p>
        </div>

        <div className="text-right">
          <p className="text-gray-500 text-sm">
            Priority Score
          </p>

          <h2
            className={`text-4xl font-bold ${
              item.total_score >= 20
                ? "text-red-600"
                : item.total_score >= 10
                ? "text-orange-500"
                : "text-green-600"
            }`}
          >
            {item.total_score}
          </h2>
        </div>
      </div>

      <div className="bg-slate-100 rounded-lg p-4">

  <p className="text-center text-sm text-gray-500">
    Complexity
  </p>

  <ProgressBar
    value={item.breakdown.complexity.cyclomatic_complexity}
    max={50}
    color="red"
  />

</div>

<div className="bg-slate-100 rounded-lg p-4">

  <p className="text-center text-sm text-gray-500">
    Issues
  </p>

  <ProgressBar
    value={item.breakdown.issues.count}
    max={10}
    color="orange"
  />

</div>

<div className="bg-slate-100 rounded-lg p-4">

  <p className="text-center text-sm text-gray-500">
    Commits
  </p>

  <ProgressBar
    value={item.breakdown.churn.commits}
    max={30}
    color="blue"
  />

</div>

      <div className="mt-6">
        <p className="font-semibold mb-2">
          Reasons
        </p>

        <div className="flex flex-wrap gap-2">
          {item.reasons.length > 0 ? (
            item.reasons.map((reason) => (
              <span
                key={reason}
                className="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm"
              >
                {reason}
              </span>
            ))
          ) : (
            <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm">
              Healthy Component
            </span>
          )}
        </div>
      </div>
    </div>
  );
}


export default RoadmapCard;