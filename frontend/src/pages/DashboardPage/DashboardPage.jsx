import { Navigate, useLocation } from "react-router-dom";

import Navbar from "../../components/Navbar/Navbar";
import RepositoryInfo from "../../components/RepositoryInfo/RepositoryInfo";
import SummaryCards from "../../components/SummaryCards/SummaryCards";
import Roadmap from "../../components/Roadmap/Roadmap";

function DashboardPage() {
  const { state } = useLocation();

  if (!state) {
    return <Navigate to="/" replace />;
  }

  const analysis = state;

  return (
    <>
      <Navbar />

      <main className="pt-28 max-w-7xl mx-auto px-6 pb-20">

        <RepositoryInfo
          repository={analysis.repository}
        />

        <SummaryCards
          repository={analysis.repository}
          summary={analysis.summary}
        />

        <Roadmap
          roadmap={analysis.roadmap}
        />

      </main>
    </>
  );
}

export default DashboardPage;