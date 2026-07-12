import { ArrowRight } from "lucide-react";

function Hero() {
  return (
    <section
      id="hero"
      className="min-h-screen pt-36 bg-linear-to-b from-blue-50 via-white to-white"
    >
      <div className="max-w-7xl mx-auto px-8 min-h-[80vh] flex flex-col lg:flex-row items-center justify-between">
        {/* Left Side */}
        <div className="max-w-2xl">
          <p className="uppercase tracking-[0.35em] text-blue-600 font-semibold">
            Analyze • Prioritize • Refactor
          </p>
          <h1 className="mt-6 text-6xl lg:text-7xl font-extrabold leading-tight text-slate-900">
            Know what to
            <br />
            refactor next.
          </h1>
          <p className="mt-8 text-xl leading-9 text-slate-600">
            Analyze GitHub repositories, uncover technical debt hotspots,
            and receive a prioritized roadmap that helps engineering teams
            focus on the changes that matter most.
          </p>

          <div className="mt-10 flex gap-4">

            <a
              href="#analyzer"
              className="
                inline-flex
                items-center
                gap-2
                bg-blue-600
                text-white
                px-8
                py-4
                rounded-2xl
                text-lg
                font-semibold
                hover:bg-blue-700
                transition
              "
            >
              Analyze Repository
              <ArrowRight size={20} />
            </a>
          </div>
        </div>
                <div
          className="
            hidden
            lg:block
            w-520
            rounded-3xl
            bg-slate-900
            shadow-2xl
            overflow-hidden
            border
            border-slate-700
          "
        >

          <div className="px-6 py-4 border-b border-slate-700 flex gap-2">

            <div className="w-3 h-3 rounded-full bg-red-500"></div>
            <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
            <div className="w-3 h-3 rounded-full bg-green-500"></div>

          </div>

          <div className="p-8 font-mono text-sm text-slate-300 space-y-4">

            <p className="text-green-400">
              $ refactoriq analyze
            </p>

            <p>
              ✓ Cloning repository...
            </p>

            <p>
              ✓ Running static analysis...
            </p>

            <p>
              ✓ Calculating complexity...
            </p>

            <p>
              ✓ Analyzing git churn...
            </p>

            <p>
              ✓ Prioritizing technical debt...
            </p>

            <div className="mt-8 rounded-xl bg-slate-800 p-4">

              <p className="text-white">
                Repository Health
              </p>

              <div className="mt-4 h-3 rounded-full bg-slate-700">

                <div
                  className="
                    h-full
                    w-3/4
                    rounded-full
                    bg-blue-500
                  "
                />

              </div>

              <p className="mt-3 text-green-400">
                Analysis Complete ✓
              </p>

            </div>

          </div>

        </div>
      </div>
    </section>
  );
}
export default Hero;