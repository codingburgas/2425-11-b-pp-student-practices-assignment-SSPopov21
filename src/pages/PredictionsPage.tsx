
import { useState } from "react";
import Header from "@/components/Header";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useJobSuccessModel, JobApplicationData, ModelPrediction } from "@/utils/mlModel";
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import { ChartLine } from "@/components/CustomIcons";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { PlusCircle } from "lucide-react";

const PredictionsPage = () => {
  // Mock data - This would be replaced with real data from your application
  const [applications] = useState<JobApplicationData[]>([
    {
      company: "TechCorp",
      position: "Senior Frontend Developer",
      date: "2025-05-18",
      status: "interview",
      priority: "high",
      followUp: true,
      applicationQuality: 85,
      skills: ["React", "TypeScript", "Tailwind CSS"]
    },
    {
      company: "DataSystems",
      position: "Machine Learning Engineer",
      date: "2025-05-15",
      status: "applied",
      priority: "medium",
      followUp: false,
      applicationQuality: 75,
      skills: ["Python", "TensorFlow", "Data Science"]
    },
    {
      company: "WebScale",
      position: "Full Stack Developer",
      date: "2025-05-10",
      status: "offer",
      priority: "high",
      followUp: true,
      applicationQuality: 90,
      skills: ["Node.js", "React", "MongoDB"]
    },
    {
      company: "CloudNative",
      position: "DevOps Engineer",
      date: "2025-05-05",
      status: "rejected",
      priority: "low",
      followUp: false,
      applicationQuality: 65,
      skills: ["Docker", "Kubernetes", "AWS"]
    }
  ]);

  // Use our ML model hook
  const { ready, getAllPredictions } = useJobSuccessModel(applications);
  
  // Get predictions for all applications
  const predictions = ready ? getAllPredictions() : new Map<string, ModelPrediction>();
  
  // Prepare data for the charts
  const successRateData = Array.from(predictions.entries()).map(([key, prediction]) => {
    const [company, position] = key.split('-');
    return {
      name: company,
      position: position,
      successRate: prediction.successProbability,
    };
  }).sort((a, b) => b.successRate - a.successRate);
  
  // Calculate average success probability
  const averageSuccessProbability = successRateData.length > 0
    ? Math.round(successRateData.reduce((acc, item) => acc + item.successRate, 0) / successRateData.length)
    : 0;
  
  // Extract key factors and their impacts
  const factorImpactData = ready && successRateData.length > 0
    ? Array.from(predictions.values())
        .flatMap(p => p.keyFactors)
        .reduce((acc, { factor, impact }) => {
          const existing = acc.find(item => item.factor === factor);
          if (existing) {
            existing.impact = (existing.impact + impact) / 2;
          } else {
            acc.push({ factor, impact });
          }
          return acc;
        }, [] as { factor: string; impact: number }[])
        .sort((a, b) => b.impact - a.impact)
    : [];

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">ML-Powered Predictions</h1>
            <p className="text-gray-600">
              Machine learning insights to improve your job application success rate
            </p>
          </div>
          <Link to="/add">
            <Button className="flex items-center gap-2">
              <PlusCircle className="h-4 w-4" />
              Add Application
            </Button>
          </Link>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <Card className="md:col-span-3">
            <CardHeader>
              <CardTitle className="flex items-center">
                <ChartLine className="mr-2" />
                Success Probability Predictions
              </CardTitle>
            </CardHeader>
            <CardContent>
              {ready ? (
                <div className="w-full overflow-x-auto">
                  <BarChart
                    width={800}
                    height={300}
                    data={successRateData}
                    margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
                  >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis label={{ value: 'Success Probability (%)', angle: -90, position: 'insideLeft' }} />
                    <Tooltip formatter={(value) => [`${value}%`, 'Success Probability']} />
                    <Bar dataKey="successRate" fill="#3b82f6" name="Success Probability" />
                  </BarChart>
                </div>
              ) : (
                <div className="flex justify-center items-center h-72">
                  <p className="text-gray-500">Loading model predictions...</p>
                </div>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Overall Success</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-6">
                <div>
                  <div className="flex justify-between mb-2">
                    <span className="text-sm font-medium">Average Success Rate</span>
                    <span className="text-sm font-medium">{averageSuccessProbability}%</span>
                  </div>
                  <Progress value={averageSuccessProbability} className="h-2" />
                </div>
                
                <div>
                  <span className="text-sm font-medium">Top Factors For Success</span>
                  <div className="mt-3 space-y-2">
                    {factorImpactData.slice(0, 3).map((factor, index) => (
                      <div key={index} className="flex justify-between items-center">
                        <span className="text-xs">{factor.factor}</span>
                        <Badge variant="outline">{factor.impact}%</Badge>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <Card>
            <CardHeader>
              <CardTitle>Application Success Factors</CardTitle>
            </CardHeader>
            <CardContent>
              {ready ? (
                <div className="w-full overflow-x-auto">
                  <BarChart
                    width={500}
                    height={300}
                    data={factorImpactData}
                    margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
                    layout="vertical"
                  >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis type="number" />
                    <YAxis type="category" dataKey="factor" width={150} />
                    <Tooltip formatter={(value) => [`${value}%`, 'Impact']} />
                    <Bar dataKey="impact" fill="#10b981" name="Impact %" />
                  </BarChart>
                </div>
              ) : (
                <div className="flex justify-center items-center h-72">
                  <p className="text-gray-500">Loading factor data...</p>
                </div>
              )}
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Recommended Actions</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {Array.from(predictions.entries()).map(([key, prediction], idx) => {
                  if (prediction.recommendedActions.length === 0) return null;
                  
                  const [company] = key.split('-');
                  return (
                    <div key={idx} className="border-b pb-3 last:border-b-0">
                      <h3 className="font-medium text-gray-900 mb-1">{company}</h3>
                      <ul className="space-y-1">
                        {prediction.recommendedActions.map((action, i) => (
                          <li key={i} className="text-sm flex items-start">
                            <span className="text-blue-500 mr-2">•</span>
                            <span>{action}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  );
                })}
                
                {!ready || Array.from(predictions.values()).every(p => p.recommendedActions.length === 0) ? (
                  <p className="text-gray-500">No specific recommendations available.</p>
                ) : null}
              </div>
            </CardContent>
          </Card>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Application Details with ML Insights</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="overflow-x-auto">
              <table className="w-full border-collapse">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="text-left py-3 px-4 font-medium text-gray-500 border-b">Company</th>
                    <th className="text-left py-3 px-4 font-medium text-gray-500 border-b">Position</th>
                    <th className="text-left py-3 px-4 font-medium text-gray-500 border-b">Status</th>
                    <th className="text-left py-3 px-4 font-medium text-gray-500 border-b">Success Probability</th>
                    <th className="text-left py-3 px-4 font-medium text-gray-500 border-b">Top Factor</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-100">
                  {applications.map((app, idx) => {
                    const key = `${app.company}-${app.position}`;
                    const prediction = predictions.get(key);
                    const topFactor = prediction?.keyFactors[0];
                    
                    return (
                      <tr key={idx} className="hover:bg-gray-50">
                        <td className="py-3 px-4">{app.company}</td>
                        <td className="py-3 px-4">{app.position}</td>
                        <td className="py-3 px-4">
                          <Badge className={app.status === 'offer' ? 'bg-green-100 text-green-800' : 
                                           app.status === 'interview' ? 'bg-yellow-100 text-yellow-800' :
                                           app.status === 'rejected' ? 'bg-red-100 text-red-800' : 
                                           'bg-blue-100 text-blue-800'}>
                            {app.status.charAt(0).toUpperCase() + app.status.slice(1)}
                          </Badge>
                        </td>
                        <td className="py-3 px-4">
                          {prediction ? (
                            <div className="flex items-center">
                              <span className="mr-2">{prediction.successProbability}%</span>
                              <Progress value={prediction.successProbability} className="h-1 w-20" />
                            </div>
                          ) : (
                            "N/A"
                          )}
                        </td>
                        <td className="py-3 px-4">
                          {topFactor ? `${topFactor.factor} (${topFactor.impact}%)` : "N/A"}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </CardContent>
        </Card>
      </main>
    </div>
  );
};

export default PredictionsPage;
