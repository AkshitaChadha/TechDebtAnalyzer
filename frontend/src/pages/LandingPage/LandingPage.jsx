import Navbar from "../../components/Navbar/Navbar";

import Hero from "../../sections/Hero/Hero";
import Features from "../../sections/Features/Features";
import HowItWorks from "../../sections/HowItWorks/HowItWorks";
import Analyzer from "../../sections/Analyzer/Analyzer";
import Footer from "../../sections/Footer/Footer";

function LandingPage() {
  return (
    <>
      <Navbar />

      <Hero />

      <Features />

      <HowItWorks />

      <Analyzer />

      <Footer />
    </>
  );
}

export default LandingPage;