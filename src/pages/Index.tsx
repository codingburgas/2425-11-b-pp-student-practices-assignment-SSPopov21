
import { Button } from "@/components/ui/button";
import { PlusCircle, ChartLine } from "lucide-react";
import { Link } from "react-router-dom";
import Header from "@/components/Header";
import SuccessMetrics from "@/components/SuccessMetrics";
import JobList from "@/components/JobList";
import SuccessFactors from "@/components/SuccessFactors";

const Index = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Job Application Dashboard</h1>
          <div className="flex space-x-3">
            <Link to="/predictions">
              <Button variant="outline" className="flex items-center gap-2">
                <ChartLine className="h-4 w-4" />
                ML Predictions
              </Button>
            </Link>
            <Link to="/add">
              <Button className="flex items-center gap-2">
                <PlusCircle className="h-4 w-4" />
                Add Application
              </Button>
            </Link>
          </div>
        </div>
        
        <SuccessMetrics />
        
        <div className="grid grid-cols-1 gap-8 mb-8">
          <JobList />
        </div>
        
        <div className="grid grid-cols-1 gap-8">
          <SuccessFactors />
        </div>
      </main>
    </div>
  );
};

export default Index;
