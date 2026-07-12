import {
  FileCode2,
  Boxes,
  TriangleAlert,
  Flame,
} from "lucide-react";

const icons = {
  "Python Files": FileCode2,
  "Entities": Boxes,
  "Issues": TriangleAlert,
  "High Priority": Flame,
};

function SummaryCard({ title, value }) {
  const Icon = icons[title];

  return (
    <div className="bg-white rounded-xl shadow-md border border-slate-200 p-6 hover:shadow-xl transition duration-300">
      <div className="flex justify-center mb-3">
        <Icon
          size={28}
          className="text-blue-600"
        />
      </div>

      <p className="text-gray-500 text-sm text-center">
        {title}
      </p>

      <h2 className="text-4xl font-bold text-center mt-2 text-slate-800">
        {value}
      </h2>
    </div>
  );
}

export default SummaryCard;