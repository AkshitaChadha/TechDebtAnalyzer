import { ArrowRight, GitBranch } from "lucide-react";
import logo from "../../assets/logo/refactor_icon_black_logo.jpg";

function Navbar() {
  return (
    <header className="fixed top-0 left-0 right-0 z-50">
      <nav
        className="
          max-w-7xl
          mx-auto
          mt-5
          px-8
          h-16
          bg-white/70
          backdrop-blur-2xl
          border
          border-slate-200/70
          rounded-2xl
          shadow-lg
          flex
          items-center
          justify-between
        "
      >
        <a href="/#hero" className="flex items-center">
          <img
            src={logo}
            alt="RefactorIQ"
            className="h-11"
          />
        </a>

        <div className="hidden md:flex items-center gap-10 font-medium text-slate-600">
          <a
            href="/#features"
            className="transition hover:text-blue-600"
          >
            Features
          </a>

          <a
            href="/#how-it-works"
            className="transition hover:text-blue-600"
          >
            How It Works
          </a>

          <a
            href="/#analyzer"
            className="transition hover:text-blue-600"
          >
            Analyze
          </a>
        </div>

        <div className="flex items-center gap-3">
          <a
            href="https://github.com"
            target="_blank"
            rel="noreferrer"
            className="
              hidden
              md:flex
              items-center
              gap-2
              px-5
              py-2.5
              rounded-xl
              border
              border-slate-300
              text-slate-700
              hover:bg-slate-100
              transition
            "
          >
            <GitBranch size={18} />
            GitHub
          </a>

          <a
            href="/#analyzer"
            className="
              flex
              items-center
              gap-2
              px-6
              py-2.5
              rounded-xl
              bg-blue-600
              text-white
              hover:bg-blue-700
              transition
            "
          >
            Analyze
            <ArrowRight size={18} />
          </a>
        </div>
      </nav>
    </header>
  );
}

export default Navbar;