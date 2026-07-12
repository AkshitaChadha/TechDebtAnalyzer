function ProgressBar({ value, max = 50, color = "blue" }) {
  const percentage = Math.min((value / max) * 100, 100);

  const colors = {
    red: "bg-red-500",
    orange: "bg-orange-500",
    green: "bg-green-500",
    blue: "bg-blue-500",
  };

  return (
    <div>
      <div className="w-full bg-slate-200 rounded-full h-2 overflow-hidden">
        <div
          className={`${colors[color]} h-2 transition-all duration-700`}
          style={{ width: `${percentage}%` }}
        />
      </div>

      <p className="text-center mt-2 font-semibold">
        {value}
      </p>
    </div>
  );
}

export default ProgressBar;