function RepositoryForm({
  repoUrl,
  setRepoUrl,
  onAnalyze,
  loading,
}) {
  return (
    <div className="flex gap-4">

      <input
        className="flex-1 border rounded-lg px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500"
        placeholder="Paste a GitHub repository URL..."
        value={repoUrl}
        onChange={(e) => setRepoUrl(e.target.value)}
      />

      <button
        onClick={onAnalyze}
        disabled={loading}
        className="bg-blue-600 hover:bg-blue-700 disabled:bg-blue-400 text-white px-6 rounded-lg transition"
      >
        {loading ? (
          <div className="flex items-center gap-2">
            <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>

            Analyzing...
          </div>
        ) : (
          "Analyze Repository"
        )}
      </button>

    </div>
  );
}

export default RepositoryForm;