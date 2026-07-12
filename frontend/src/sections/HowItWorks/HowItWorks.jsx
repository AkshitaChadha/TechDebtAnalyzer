import {
  FolderGit2,
  ScanSearch,
  BarChart3,
  Sparkles,
  ArrowRight,
} from "lucide-react";

function HowItWorks() {
  const steps = [
    {
      icon: FolderGit2,
      title: "Connect Repository",
      description: "Paste any public GitHub repository URL.",
    },
    {
      icon: ScanSearch,
      title: "Analyze Code",
      description: "RefactorIQ scans complexity, code quality and Git history.",
    },
    {
      icon: BarChart3,
      title: "Prioritize Hotspots",
      description: "Technical debt is ranked using intelligent scoring.",
    },
    {
      icon: Sparkles,
      title: "Refactor Smarter",
      description: "Receive a clear roadmap with actionable insights.",
    },
  ];

  return (
    <section className="py-28 bg-slate-50">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center">
          <p className="uppercase tracking-widest text-blue-600 font-semibold">
            HOW IT WORKS
          </p>

          <h2 className="text-5xl font-bold mt-4">
            Four steps to cleaner code.
          </h2>

          <p className="text-slate-500 mt-6 text-lg max-w-3xl mx-auto">
            RefactorIQ transforms repository analysis into an actionable
            refactoring roadmap in just a few seconds.
          </p>
        </div>

        <div id="how-it-works"  className="py-28 bg-white scroll-mt-32" className="grid lg:grid-cols-4 gap-8 mt-20">
          {steps.map((step, index) => {
            const Icon = step.icon;

            return (
              <div
                key={step.title}
                className="relative text-center"
              >
                <div className="w-20 h-20 rounded-full bg-blue-600 flex items-center justify-center mx-auto shadow-lg">
                  <Icon size={34} className="text-white" />
                </div>

                <div className="mt-6 text-sm font-bold text-blue-600">
                  STEP {index + 1}
                </div>

                <h3 className="mt-2 text-2xl font-bold">
                  {step.title}
                </h3>

                <p className="mt-4 text-slate-600 leading-7">
                  {step.description}
                </p>

                {index !== steps.length - 1 && (
                  <ArrowRight
                    className="
                      hidden
                      lg:block
                      absolute
                      top-10
                      -right-7
                      text-slate-300
                    "
                    size={28}
                  />
                )}
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}

export default HowItWorks;