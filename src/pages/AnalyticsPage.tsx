
import { useState } from "react";
import Header from "@/components/Header";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { 
  BarChart,
  Bar,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  PieChart,
  Pie,
  Cell,
} from 'recharts';

const AnalyticsPage = () => {
  const [activeTab, setActiveTab] = useState("overview");
  
  // Mock data - would come from calculations in a real app
  const applicationData = [
    { month: 'Jan', applications: 5, responses: 2, interviews: 1 },
    { month: 'Feb', applications: 8, responses: 3, interviews: 2 },
    { month: 'Mar', applications: 12, responses: 5, interviews: 3 },
    { month: 'Apr', applications: 15, responses: 7, interviews: 4 },
    { month: 'May', applications: 10, responses: 4, interviews: 2 },
  ];

  const statusData = [
    { name: 'Applied', value: 28 },
    { name: 'Interview', value: 12 },
    { name: 'Offer', value: 3 },
    { name: 'Rejected', value: 15 },
  ];

  const skillsData = [
    { name: 'React', count: 18 },
    { name: 'JavaScript', count: 22 },
    { name: 'TypeScript', count: 15 },
    { name: 'Node.js', count: 12 },
    { name: 'Python', count: 8 },
    { name: 'Data Science', count: 5 },
  ];

  const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8', '#82ca9d'];

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Analytics & Insights</h1>
          <p className="text-gray-600">
            Track your application progress and identify improvement opportunities
          </p>
        </div>

        <Tabs defaultValue="overview" value={activeTab} onValueChange={setActiveTab}>
          <TabsList className="mb-8">
            <TabsTrigger value="overview">Overview</TabsTrigger>
            <TabsTrigger value="status">Application Status</TabsTrigger>
            <TabsTrigger value="skills">Skills Analysis</TabsTrigger>
          </TabsList>
          
          <TabsContent value="overview">
            <Card className="shadow-md mb-8">
              <CardHeader>
                <CardTitle>Application Progress Over Time</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="w-full overflow-x-auto">
                  <LineChart
                    width={800}
                    height={400}
                    data={applicationData}
                    margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
                  >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="month" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="applications" stroke="#8884d8" name="Applications" />
                    <Line type="monotone" dataKey="responses" stroke="#82ca9d" name="Responses" />
                    <Line type="monotone" dataKey="interviews" stroke="#ffc658" name="Interviews" />
                  </LineChart>
                </div>
                
                <div className="mt-6 text-center text-sm text-gray-600">
                  <p>Success rate (Interviews / Applications): 20%</p>
                  <p>Average response time: 5 days</p>
                </div>
              </CardContent>
            </Card>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <Card className="shadow-md">
                <CardHeader>
                  <CardTitle>Application Improvement Tips</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-4">
                    <li className="flex items-start">
                      <span className="inline-flex items-center justify-center w-6 h-6 rounded-full bg-blue-100 text-blue-600 mr-3 text-xs">1</span>
                      <span>
                        <strong>Customize each resume</strong>
                        <p className="text-sm text-gray-600">
                          Tailor your resume to match job keywords for better ATS results
                        </p>
                      </span>
                    </li>
                    <li className="flex items-start">
                      <span className="inline-flex items-center justify-center w-6 h-6 rounded-full bg-blue-100 text-blue-600 mr-3 text-xs">2</span>
                      <span>
                        <strong>Apply earlier</strong>
                        <p className="text-sm text-gray-600">
                          Applications submitted within 48 hours get 8x more responses
                        </p>
                      </span>
                    </li>
                    <li className="flex items-start">
                      <span className="inline-flex items-center justify-center w-6 h-6 rounded-full bg-blue-100 text-blue-600 mr-3 text-xs">3</span>
                      <span>
                        <strong>Follow up</strong>
                        <p className="text-sm text-gray-600">
                          A brief follow-up after 1 week increases response chance by 30%
                        </p>
                      </span>
                    </li>
                    <li className="flex items-start">
                      <span className="inline-flex items-center justify-center w-6 h-6 rounded-full bg-blue-100 text-blue-600 mr-3 text-xs">4</span>
                      <span>
                        <strong>Network connections</strong>
                        <p className="text-sm text-gray-600">
                          Referrals are 15x more likely to be hired than direct applications
                        </p>
                      </span>
                    </li>
                  </ul>
                </CardContent>
              </Card>
              
              <Card className="shadow-md">
                <CardHeader>
                  <CardTitle>Current Application Status</CardTitle>
                </CardHeader>
                <CardContent className="flex justify-center">
                  <PieChart width={300} height={300}>
                    <Pie
                      data={statusData}
                      cx={150}
                      cy={150}
                      labelLine={false}
                      outerRadius={100}
                      fill="#8884d8"
                      dataKey="value"
                      label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                    >
                      {statusData.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                      ))}
                    </Pie>
                    <Tooltip />
                  </PieChart>
                </CardContent>
              </Card>
            </div>
          </TabsContent>
          
          <TabsContent value="status">
            <Card className="shadow-md mb-8">
              <CardHeader>
                <CardTitle>Applications by Status</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex justify-center">
                  <PieChart width={400} height={400}>
                    <Pie
                      data={statusData}
                      cx={200}
                      cy={200}
                      labelLine={false}
                      outerRadius={160}
                      fill="#8884d8"
                      dataKey="value"
                      label={({ name, value, percent }) => `${name}: ${value} (${(percent * 100).toFixed(0)}%)`}
                    >
                      {statusData.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                      ))}
                    </Pie>
                    <Tooltip />
                    <Legend />
                  </PieChart>
                </div>
                
                <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div className="bg-white p-5 rounded-lg border border-gray-200">
                    <h3 className="text-lg font-semibold mb-3">Response Rate</h3>
                    <div className="flex items-center justify-between">
                      <span className="text-3xl font-bold text-blue-600">32%</span>
                      <span className="text-sm text-gray-500">Applications that received any response</span>
                    </div>
                  </div>
                  
                  <div className="bg-white p-5 rounded-lg border border-gray-200">
                    <h3 className="text-lg font-semibold mb-3">Interview Rate</h3>
                    <div className="flex items-center justify-between">
                      <span className="text-3xl font-bold text-green-600">18%</span>
                      <span className="text-sm text-gray-500">Applications that led to interviews</span>
                    </div>
                  </div>
                  
                  <div className="bg-white p-5 rounded-lg border border-gray-200">
                    <h3 className="text-lg font-semibold mb-3">Offer Rate</h3>
                    <div className="flex items-center justify-between">
                      <span className="text-3xl font-bold text-yellow-600">5%</span>
                      <span className="text-sm text-gray-500">Applications that led to job offers</span>
                    </div>
                  </div>
                  
                  <div className="bg-white p-5 rounded-lg border border-gray-200">
                    <h3 className="text-lg font-semibold mb-3">Average Response Time</h3>
                    <div className="flex items-center justify-between">
                      <span className="text-3xl font-bold text-purple-600">5 days</span>
                      <span className="text-sm text-gray-500">From application to first response</span>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
          
          <TabsContent value="skills">
            <Card className="shadow-md">
              <CardHeader>
                <CardTitle>Skills Analysis</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="w-full overflow-x-auto">
                  <BarChart
                    width={800}
                    height={400}
                    data={skillsData}
                    margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
                  >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Bar dataKey="count" name="Job Postings Requiring" fill="#8884d8" />
                  </BarChart>
                </div>
                
                <div className="mt-8">
                  <h3 className="text-lg font-semibold mb-4">Skill Improvement Recommendations</h3>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="bg-white p-4 rounded-lg border border-gray-200">
                      <h4 className="font-medium text-primary">TypeScript</h4>
                      <p className="text-sm text-gray-600">
                        Appears in 65% of job postings. Consider adding more advanced TypeScript projects to your portfolio.
                      </p>
                    </div>
                    
                    <div className="bg-white p-4 rounded-lg border border-gray-200">
                      <h4 className="font-medium text-primary">React</h4>
                      <p className="text-sm text-gray-600">
                        Appears in 78% of job postings. Focus on React hooks and context API in your resume.
                      </p>
                    </div>
                    
                    <div className="bg-white p-4 rounded-lg border border-gray-200">
                      <h4 className="font-medium text-primary">Python</h4>
                      <p className="text-sm text-gray-600">
                        Growing demand in web development roles. Consider adding a Python project to your portfolio.
                      </p>
                    </div>
                    
                    <div className="bg-white p-4 rounded-lg border border-gray-200">
                      <h4 className="font-medium text-primary">Testing</h4>
                      <p className="text-sm text-gray-600">
                        Mentioned in 45% of job posts but missing in your profile. Add experience with Jest and React Testing Library.
                      </p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </main>
    </div>
  );
};

export default AnalyticsPage;
