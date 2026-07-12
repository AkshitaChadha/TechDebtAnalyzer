import {
  BarChart3,
  GitCommitHorizontal,
  BrainCircuit,
  ArrowRight,
} from "lucide-react";

function Features() {
  const features = [
    {
      title: "Complexity Analysis",
      description:
        "Measure cyclomatic complexity and identify difficult-to-maintain code before it becomes technical debt.",
      icon: BarChart3,
    },
    {
      title: "Git Churn Intelligence",
      description:
        "Analyze commit history to discover unstable components that deserve immediate engineering attention.",
      icon: GitCommitHorizontal,
    },
    {
      title: "Smart Prioritization",
      description:
        "Combine complexity, code quality and churn into a practical roadmap for confident refactoring.",
      icon: BrainCircuit,
    },
  ];

  return (
    <section className="py-28 bg-white">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center">
          <p className="text-blue-600 font-semibold uppercase tracking-widest">
            FEATURES
          </p>

          <h2 className="text-5xl font-bold mt-4 text-slate-900">
            Built for developers.
          </h2>

          <p className="text-slate-500 mt-6 max-w-3xl mx-auto text-lg leading-8">
            RefactorIQ helps engineering teams discover technical debt,
            prioritize refactoring work, and improve long-term code quality.
          </p>
        </div>

        <div id="features"  className="py-28 bg-white scroll-mt-32" className="grid lg:grid-cols-3 gap-8 mt-20">
          {features.map((feature) => {
            const Icon = feature.icon;

            return (
              <div
                key={feature.title}
                className="
                  group
                  rounded-3xl
                  border
                  border-slate-200
                  bg-white
                  p-8
                  shadow-sm
                  transition-all
                  duration-300
                  hover:-translate-y-2
                  hover:shadow-2xl
                  hover:border-blue-500
                "
              >
                <div
                  className="
                    w-16
                    h-16
                    rounded-2xl
                    bg-blue-100
                    flex
                    items-center
                    justify-center
                    transition-all
                    duration-300
                    group-hover:bg-blue-600
                  "
                >
                  <Icon
                    size={32}
                    className="text-blue-600 group-hover:text-white"
                  />
                </div>

                <h3 className="text-2xl font-bold mt-8">
                  {feature.title}
                </h3>

                <p className="text-slate-600 mt-5 leading-8">
                  {feature.description}
                </p>

                <button
                  className="
                    mt-8
                    flex
                    items-center
                    gap-2
                    text-blue-600
                    font-semibold
                    group-hover:gap-4
                    transition-all
                  "
                >
                  Learn More
                  <ArrowRight size={18} />
                </button>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}

export default Features;