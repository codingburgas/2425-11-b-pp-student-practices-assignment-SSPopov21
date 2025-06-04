
import Header from "@/components/Header";
import AddJobForm from "@/components/AddJobForm";

const AddJobPage = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Add Job Application</h1>
          <p className="text-gray-600">
            Track a new job application to monitor its progress and increase your chances of success
          </p>
        </div>
        
        <div className="max-w-4xl mx-auto">
          <AddJobForm />
        </div>
      </main>
    </div>
  );
};

export default AddJobPage;
