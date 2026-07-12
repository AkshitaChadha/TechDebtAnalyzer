import { GitBranch } from "lucide-react";
function RepositoryInfo({ repository }) {
  return (
    <div className="mt-10 mb-8">
      <div className="flex items-center gap-3">
        <GitBranch
            className="text-slate-700"
        />
        <div>
          <h2 className="text-2xl font-bold">
            {repository.name}
          </h2>
          <p className="text-gray-500">
            Repository Analysis
          </p>
        </div>
      </div>
    </div>
  );
}
export default RepositoryInfo;
