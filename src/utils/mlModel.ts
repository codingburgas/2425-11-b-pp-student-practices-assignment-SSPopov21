
import { useEffect, useState } from 'react';

// Simple interface for job application data
export interface JobApplicationData {
  company: string;
  position: string;
  date: string;
  status: 'applied' | 'interview' | 'offer' | 'rejected';
  priority: 'low' | 'medium' | 'high';
  skills: string[];
  location?: string;
  salary?: number;
  followUp?: boolean;
  applicationQuality?: number;
}

// Interface for model predictions
export interface ModelPrediction {
  successProbability: number;
  recommendedActions: string[];
  keyFactors: { factor: string; impact: number }[];
}

// Simplified ML model implementation using NumPy-like operations in TypeScript
export class JobSuccessModel {
  // Mock weights for different factors
  private weights = {
    skills: 0.35,
    followUp: 0.15,
    applicationQuality: 0.25,
    companySize: 0.10,
    timeToApplication: 0.15,
  };

  // Features extracted from application data
  private extractFeatures(application: JobApplicationData, allApplications: JobApplicationData[]): number[] {
    // Count how many in-demand skills this application has
    const inDemandSkills = ['React', 'TypeScript', 'Python', 'Data Science', 'Machine Learning'];
    const skillsMatch = application.skills.filter(s => 
      inDemandSkills.includes(s)).length / inDemandSkills.length;
    
    // Check if follow-up was done
    const followUpScore = application.followUp ? 1.0 : 0.0;
    
    // Application quality score
    const qualityScore = application.applicationQuality ? application.applicationQuality / 100 : 0.5;
    
    // Company size estimation (based on similar applications)
    const companyFactor = Math.random() * 0.5 + 0.5; // Simple random factor between 0.5-1.0
    
    // Time to application after job posting (simulated)
    const timeApplicationFactor = Math.random() * 0.7 + 0.3; // Random between 0.3-1.0
    
    return [skillsMatch, followUpScore, qualityScore, companyFactor, timeApplicationFactor];
  }

  // NumPy-like array operations
  private dotProduct(a: number[], b: number[]): number {
    return a.reduce((sum, val, i) => sum + val * b[i], 0);
  }

  // Sigmoid function for probability
  private sigmoid(x: number): number {
    return 1 / (1 + Math.exp(-x));
  }

  // Predict success probability
  public predict(application: JobApplicationData, allApplications: JobApplicationData[]): ModelPrediction {
    const features = this.extractFeatures(application, allApplications);
    const weightValues = Object.values(this.weights);
    
    // Calculate raw score (dot product)
    const rawScore = this.dotProduct(features, weightValues);
    
    // Convert to probability
    const probability = this.sigmoid(rawScore * 2 - 1) * 100;
    
    // Generate recommendations based on feature analysis
    const recommendations: string[] = [];
    const factors: { factor: string; impact: number }[] = [];
    
    // Generate factor impacts
    Object.entries(this.weights).forEach(([key, weight], index) => {
      const impact = features[index] * weight * 100;
      let factorName = '';
      
      switch(key) {
        case 'skills':
          factorName = 'Skills Match';
          if (features[index] < 0.5) {
            recommendations.push('Add more relevant skills to your application');
          }
          break;
        case 'followUp':
          factorName = 'Follow-up';
          if (features[index] < 0.9) {
            recommendations.push('Follow up on your application after 5-7 days');
          }
          break;
        case 'applicationQuality':
          factorName = 'Application Quality';
          if (features[index] < 0.7) {
            recommendations.push('Improve your resume and cover letter quality');
          }
          break;
        case 'companySize':
          factorName = 'Company Fit';
          break;
        case 'timeToApplication':
          factorName = 'Application Timing';
          if (features[index] < 0.5) {
            recommendations.push('Apply earlier to job postings for better results');
          }
          break;
      }
      
      factors.push({ factor: factorName, impact: Math.round(impact) });
    });
    
    // Sort factors by impact
    factors.sort((a, b) => b.impact - a.impact);
    
    return {
      successProbability: Math.round(probability),
      recommendedActions: recommendations,
      keyFactors: factors,
    };
  }
}

// Custom hook to use the model in React components
export function useJobSuccessModel(applications: JobApplicationData[]) {
  const [model, setModel] = useState<JobSuccessModel | null>(null);

  useEffect(() => {
    // Initialize model on component mount
    setModel(new JobSuccessModel());
  }, []);

  // Function to get prediction for a single application
  const getPrediction = (application: JobApplicationData): ModelPrediction | null => {
    if (!model) return null;
    
    return model.predict(application, applications);
  };

  // Function to get predictions for all applications
  const getAllPredictions = (): Map<string, ModelPrediction> => {
    const predictions = new Map<string, ModelPrediction>();
    
    if (!model) return predictions;
    
    applications.forEach(app => {
      const key = `${app.company}-${app.position}`;
      predictions.set(key, model.predict(app, applications));
    });
    
    return predictions;
  };

  return {
    ready: model !== null,
    getPrediction,
    getAllPredictions,
  };
}
