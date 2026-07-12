import { useState } from "react";

import RepositoryForm from "../../components/RepositoryForm/RepositoryForm";
import RepositoryInfo from "../../components/RepositoryInfo/RepositoryInfo";
import SummaryCards from "../../components/SummaryCards/SummaryCards";
import Roadmap from "../../components/Roadmap/Roadmap";
import { useNavigate } from "react-router-dom";

import { analyzeRepository } from "../../api/analysis";

function Analyzer() {

    const [repoUrl, setRepoUrl] = useState("");
    const [analysis, setAnalysis] = useState(null);
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    async function handleAnalyze() {

        try {

            setLoading(true);

            const data = await analyzeRepository(repoUrl);

            navigate("/dashboard", {
                state: data,
            });
            

        }

        catch (error) {

            console.error(error);

            alert("Analysis failed.");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <section
            id="analyzer"
            className="py-24 bg-slate-100"
        >

            <div className="max-w-6xl mx-auto">

                            <div className="bg-white rounded-3xl shadow-xl p-10">

                                <div className="text-center mb-10">
                <p className="uppercase tracking-widest text-blue-600 font-semibold">
                    ANALYZE
                </p>

                <h2 className="text-5xl font-bold mt-4">
                    Ready to analyze your repository?
                </h2>

                <p className="text-slate-500 mt-6 max-w-2xl mx-auto text-lg leading-8">
                    Paste a public GitHub repository URL to uncover technical debt,
                    identify refactoring hotspots, and generate an intelligent roadmap.
                </p>
            </div>

                    <RepositoryForm
                        repoUrl={repoUrl}
                        setRepoUrl={setRepoUrl}
                        onAnalyze={handleAnalyze}
                        loading={loading}
                      />

                    {loading && (
                        <div  className="py-28 bg-white scroll-mt-32" className="mt-12 text-center">
                            <div className="inline-block h-12 w-12 border-4 border-blue-600 border-t-transparent rounded-full animate-spin" />

                            <p className="mt-6 text-slate-600 text-lg">
                                Analyzing repository...
                            </p>

                            <p className="text-slate-400 mt-2">
                                Computing complexity, issues and Git churn.
                            </p>
                        </div>
                    )}

                    

                </div>

            </div>

        </section>

    );

}

export default Analyzer;