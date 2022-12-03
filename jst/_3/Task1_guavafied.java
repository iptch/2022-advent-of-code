package _3;

import java.util.Set;
import java.util.stream.Collectors;

import static com.google.common.collect.Sets.intersection;

public class Task1_guavafied {

    public static void main(String[] args) {
        String input = getInput();
        String[] lines = input.split("\n");

        int result = 0;

        for (String line : lines) {
            String firstHalf = line.substring(0, line.length() / 2);
            String secondHalf = line.substring(line.length() / 2);

            Integer character = intersection(chars(firstHalf), chars(secondHalf)).iterator().next();

            int value = Character.isLowerCase(character) ? (character - ('a') + 1) : (character - 'A' + 27);
            result += value;
        }

        System.out.println(result);
    }

    private static Set<Integer> chars(String firstHalf) {
        return firstHalf.chars().boxed().collect(Collectors.toSet());
    }

    private static String getInput() {
        return "BccTFfTPTsffdDDqsq\n" +
                "lGGLQwFhDgWdqvhW\n" +
                "wbLNjGjlwLFrpSbllrHnHHRmmJVBmZJRRVcBTc\n" +
                "vvGLllBBLtllJnJFMZNjFcNG\n" +
                "bdhrhTgmhRrpLJMMNJgNffnf\n" +
                "qhRmTpzpzVzmTTbmVhWWWpVvDtsLVlwBVHvSsDCvvBDl\n" +
                "sLlhhthVRndBZzwBdV\n" +
                "PfmsPsqsGFqrSQpqBDDwpddDDM\n" +
                "mFjvSFrjPSvLJWvbRssN\n" +
                "gWnWQtMMDQbQvMDjjcwsvqcwsSSqZq\n" +
                "HzPJTtmtZJJsqfBJ\n" +
                "hCFPrNNPVNzFtQhdQMWRhhDd\n" +
                "sNhmsQZdNdsztNpHGCdjcBcwCvGvCv\n" +
                "brSlRfFFppHwfTpf\n" +
                "MbRlRpqMnqRpMhVtsQQQVWsM\n" +
                "HsdttdfHrHrwdhftMHMSDnJFwlQSgQZQZggZSW\n" +
                "LjCTqBCmmmTqgFQQFQjlnnDJ\n" +
                "GCTLBCmTBDBDPTTzqLCBpVcctcHbtbrcMMsdsdtcPtdb\n" +
                "QnJLdNLfLRQjpLlPflfQnlnswRvwsHVWVHWVVDZwWHcrwV\n" +
                "zFbgtqCBhtgBhsDZVDNHwvDv\n" +
                "zgCGCFCFGtMpJjlGTnlnLN\n" +
                "ZFhJZbvZVmFpFnJbnZFbLnbHPrjjQdBdCrMPQMQHrrrrVC\n" +
                "gTzlqmNlTflmtTRHdDPqMjHDMrjdQd\n" +
                "wcRSwglcNSwgWmNzwNlJZLpphbbnFhvLWhnphb\n" +
                "lRRrcbRfQmwwBLSLlvjjSvvFtS\n" +
                "WbghzhHWbsdHhVtGLVSSvLFJtSGC\n" +
                "WWbWzPHDqPfBqRZrmqnZ\n" +
                "frgLHMcHLrSZHPHcHrPNmMJtTCTCbJfhdwVbfJwwTbdd\n" +
                "DpDWRjQvqjDGFWhdVwQCnJgTnTbT\n" +
                "vvqggRsRpcssPrcsrN\n" +
                "MccbcZjmbbNSbjllbRqrhstVTMtqRtssTW\n" +
                "qJdwCLdCzQQzwHLQLTtsTtsTRVTVWWTJst\n" +
                "GdnpFHzwQCdpvpbccPbSbq\n" +
                "CbQhZpTbTgMMgptzrdGtGzlVNlrh\n" +
                "FWvmmRHSmjqnSjqnSjPqjnmNLGVGJlGWLlLrLWlVrGzNGW\n" +
                "FwvvBjmBnqmVvFnvnVPMDspDQTfZMCMTgDQTCB\n" +
                "VmrsHllHVLTdZtRclL\n" +
                "bjwMNQGCjGjjPwpRQnRLTtRQFvcdvt\n" +
                "MbWgjMDpNLMjNpwGpjbPWgfsHsqsHSrrHHJsgBSBzB\n" +
                "HFlwVhfLBZZLTLFHwqWCqWwQpWwSpqWC\n" +
                "PttsNjdtPtcmcDTnDdtjjDMpCCCCmSmqqGqmvMvbCqpC\n" +
                "jndRrTtPdgNPPnLrVhVLHhVJHffV\n" +
                "NJZVqHNNNJNqCdqZZVjtzCDMtzrtrFhhMFsPCS\n" +
                "TbwgwWRdQgfggQgvMPDSPszhSbSDszFs\n" +
                "QpRmWglwTQgGWTvGRvQRdwnjNNqqqBqVlcqVVNncVVHV\n" +
                "gqBFHLFDNCBClHgbLFbllLggVSTWJVWWpjvJpSSWJjBjZvjW\n" +
                "mczdshQcsGftdmcwcfhdzQVrhJZJTZhTVTDjpWpZvvWT\n" +
                "twGdRtcGnRgDqFRC\n" +
                "fsPjCjgRpwjPpsGgQwPfSZcdSZdWVHzSzcdzHRWz\n" +
                "MBLTTBMvbMmvJTLvTDvczNdZNHdHcJNzNqSZVG\n" +
                "rTlDlbBbrsjCCGnG\n" +
                "FsmBPtzHdmmvcvdWpcWCvM\n" +
                "RMJGjGGJJGLDRNJJnfGRRSvplTDccrTwSWClvCrwww\n" +
                "nnRqNGJLVLRRZNNZzBHMHVFVmzBFbhmb\n" +
                "MmTSpBMBCCMsbbrVvwwSLb\n" +
                "RffNRFRThtqHhHHqZNrLVvwQtsGvssdvvsGb\n" +
                "DThHghZfgqhFWRNHhhRWqMCnMzzznlPnBlgzMpnPCz\n" +
                "GhlMNMdpMZHHhhRLLjqSjjqvvmSh\n" +
                "PcTJDBDcBnBbTFcDwnPTQSLqLrqvWjwWLqRSvsRmWm\n" +
                "PDcDJbQTFBCBcncgQPcDgnHgVmppHVMddmZglzVHdMmt\n" +
                "BqFJqJGpBVnJqnjjmwvrNwVPHPrd\n" +
                "ZMbQmhWstZScWjdswwwHNdzHvj\n" +
                "ZZtQCtgZQWSbMMhmMSWQfGfGDBpRJnJqTFFJBgTR\n" +
                "tVcPGGqwgJPqtJtqZZwcZffsfrcNWBnSWWFrfhWBnz\n" +
                "dRMCMQLvNssBWFFR\n" +
                "pvjjQvmDMpHLdPPtgPPTssTHsq\n" +
                "WDBlFBbGdmBrqWjhWcqZCq\n" +
                "RPSRPtncngwgwzhCwghC\n" +
                "cssVsPpVncQMRsVQpRPnRcfJfTTmTdDBLbFlDblTDDDLJf\n" +
                "CZgCCzgzsCDZDzbbBclgvcjcnnjFBqgv\n" +
                "VLGThLWhWdThlWRHVTLTTjNjjdjrnBNBcrNcqmqqcc\n" +
                "VTRWLhpLWHRMPGRGRplVhSfttJpZzwstsbDtwbJzZt\n" +
                "fqhZRLhwZwVSLbCMCJdJCHQGZWdW\n" +
                "ztvpjtpcvgzppPvjvPlDQLnMlHDGWnQDLQWDdJ\n" +
                "PpsPzjPzgLrjzBgLggzrmrVSrTSfSqFVFmVhffFm\n" +
                "qMFDRLNRRJJphbhSgStpptbj\n" +
                "rZrPZZNCCCGrlfsCzBbgstBwtvbtvbvBth\n" +
                "CfVrdndzZGrfzrzdrGddPnNCFMRDJWRDDnRWDFqFDJJFTJJT\n" +
                "dMDbndBMQWnnbDstnMbMQQwspFgsFFjRrqCCFrrprqrgjc\n" +
                "SlLzZmHZSTVGSPVmSPlSmrpFvFjjpgrpgFcvrcFcWG\n" +
                "PHZZTmNVHSWJlHPNLSzPLLHwDBJtbDbnnnMffDbwtnMndQ\n" +
                "tHBzNCztLBRBtrjvSjfnjvvzfpjj\n" +
                "gQwWqlnqWqJgJnDplfflddjdsfdpFf\n" +
                "gcwwmnDccTPWWgJbZNNbZHZCRRTrLB\n" +
                "ZhjgtrJNfDNpqbhqQmqpmb\n" +
                "cFLcwGGHwcGdwFCQjnnnVcmqmjCp\n" +
                "HvvlzjWHjFWTggWStDrDZT\n" +
                "GPjjQtPQbjwWqrmnsjmnqn\n" +
                "SNGdfLLGdlldZSSRWznFsNqFRnqsWs\n" +
                "DdMpMfZMhfZMpDfbDQQbGQVgccgcVt\n" +
                "hHGGGTlddWGgpRdcvwDCDwzgLJzCwzwgwL\n" +
                "MFSbZSnnFJWwQBNMzw\n" +
                "tSjrSFSfqjqqttPnssqjssbhGmWGhcmvldcmhHRhGRhTRf\n" +
                "qdBjBTNndbnqnLmtZmZvvtLvHd\n" +
                "hDJCpfnGhJfDPzGzzCnGPmpZZVLZvHttZHQLHgZLHt\n" +
                "JDrfCDJhGMhFhPzMrCCnrGSwswswFsblTqRlRwjcjRsqBT\n" +
                "tJPRSZCSJJCnmvvvQMrpqLVwqLqMcCCM\n" +
                "hhGGGfsdfTGlfggjMLVVFsMVwMMbqbLF\n" +
                "hdTGGhGhdhfhhwlgNfdhZnZtHHRNtZHnnZmHHzmn\n" +
                "HlgRZglZDWZgfVbdznHddTvV\n" +
                "MhShhQMSFShFPPQplMPmwppwbzdtVbFtfvfbzVbvbTntzbVT\n" +
                "lMwpmJLLLNGwBrcZCjrGCGrD\n" +
                "qjjWRLjNjtGRRWTCghNwsgwcbwmC\n" +
                "HPMBpVGMPMvvVBPswmhTbCwgmsVThT\n" +
                "vDSMSvflBlHpvMMfSSpMFWZdtZWdGWGddqfFtRqQ\n" +
                "ZmnGQfnZgdmRGQGvgnnmHCbbchhpMLrpcbLpdLpzbz\n" +
                "NBFPBWFsSVNJlFqLDLwcwrPLzzCwhp\n" +
                "qlWJqqWFJJjNqJWsFVsVqqRCggtmvvjQZgQnZQmvmHRt\n" +
                "RdCsJbdsVJtRvdzBzrBcjzMTqT\n" +
                "wNSNnnHhnwhHfBHqHjBDJMJr\n" +
                "GnSPLwlFwwLWSwpNWLSNpVZtvPsVJsmRCmtgsvsRsv\n" +
                "GPMwMMPCBPwBGsCGGWqBsslQhVQFccphvhWpmcFhVLmV\n" +
                "rbNnHLLHfHfZFfQQQZml\n" +
                "DzSDNtrztbgCMMBLLCsBts\n" +
                "rTtrVbrrhbbGGhbbbbRqccdBcdBcvRvBSRRV\n" +
                "fDqQDqLFQgQgZFMlFNRgvCNvRRvHvRBHHR\n" +
                "mfPqmFsqqsbJJtGtbt\n" +
                "vNHvgsSGSFDHvspvtSGwJwJNJrllhwhcnwJlwm\n" +
                "dqWdWfQdqQVWwnfMnlcfwzMs\n" +
                "VqQQqBRTqsBQWLppZLpFSHZbvvDt\n" +
                "gdcldHQlQndnHMzCjvCFrzjSFtbLtv\n" +
                "NJGmZZJZGTDsWWJNmDVmsCrSvfPrvTtSPbFFCFFvCT\n" +
                "BDDsmJZVBJwBRsGGDmZNBGqMdnghhcwgbngpqqMgnpgc\n" +
                "VhhvVwmvmwTPCwPwmDRgDCsgWSnfRMSWSM\n" +
                "ptHZZtlZzqbZttHbzrFqnDSMShMgSRRMngDWgrGh\n" +
                "hBttqBhBzlFhtHvTJQJTcvBQJPPv\n" +
                "FjfzfGjsjBfQfMLBNg\n" +
                "VlrppVwrpVSdScwTjVnCCQLQNCMBhWgV\n" +
                "jvtSrSjjtSZpqtHPDPJqRzGR\n" +
                "ZSmbSDswfCDDHBFFvWHJ\n" +
                "jcjcVjltntQMltnVrdNnNjdQgFzWHqzBWGWQvzHwgqqJGz\n" +
                "nccLllwwhLCCSLTmmRTP\n" +
                "HBSnnJSfHvBfNWMNrvnMrZlblFbsbHwsPFVHTsHFls\n" +
                "VLmDLhRgRbZFRwjZ\n" +
                "zQDmCLLDDLGttGGgtLvvVSfqJBSVftSnrJnN\n" +
                "CgGhbgVMNgVVbjrrtcfTDTfvTscrTvSSss\n" +
                "qqFzFBzsPZHmddmsmvWSnHJnncDfWnDJvv\n" +
                "ZwdPqdqpdPlPwdRlsdBqBMjNQjGVgbQgQhGVCCtgbR\n" +
                "CGFTTMLGPgmPfGfCwTPSSFNQDLNQnscQNccWdQLqvqds\n" +
                "pbJlzhZRHtjrbrbjHHrplRWVNsNvddZNWDQVVcnQVscs\n" +
                "pzJtlJlBhJJHJjHhfPfTTFMDmMPBMSgm\n" +
                "gzCBPDDzgvLvgPLgNThPlVZccJTmrZNV\n" +
                "sndSnpsdMSnRMRpjShhNJZJhJjrVcTljTZ\n" +
                "SRRsdnGwRSpptnfMSSpdQtfdWqvbwFgbDJJzCzqqWqWbLWWz\n" +
                "BDnsPDlmmwcnCLLLwPtFTtTtFRqjRrrSVFqn\n" +
                "dfhhzMGzWJhpMWhHWggTHJVFVSSqbqqjdRRtvqqvFrtF\n" +
                "JMGfHffhQhQTNcTTBLCQmm\n" +
                "bfZBvvRRRzFfFFLRvFzZCcQlScchLlGNhSQGGVQh\n" +
                "mwJqTbsHmjbTNcNhQGGJGcVS\n" +
                "mPTgtsnPjwHHmmmbbRDgfpdgBpzvZD\n" +
                "lSnRStHtTZdjrHjnqJglbqgchhDCPCPc\n" +
                "swFBzvBNLpBBsvszvDJhCzgDDCgbbJQzDq\n" +
                "VswvBFmvpSrShmRRMn\n" +
                "vWBBSrWnZfCWVchwhbcjVN\n" +
                "RdHQQpRPJZLTtJgNcNGgbhGh\n" +
                "zpzDzTdqQRqRzzlRDsBBnBfMmCCSZDBS\n" +
                "ZtGSZVpPDtVbQjbwBDzbbL\n" +
                "WcFvTFnTMnnMcnhmQhmhBbBQzCQjVb\n" +
                "RRWsgvgnfqgpGVNg\n" +
                "WJTrJJCzLqCqBTWLsCCqzmPPQrjwHQQGpwGHHmRPVw\n" +
                "bMvnDFnFSbSlGgnpmGQVpRjV\n" +
                "DZSdFZdQZZclsscWqWLhcBhs\n" +
                "PzLlRRNjjRQzvPNQsvddlZfchhWWZJHSlhChDhHhcc\n" +
                "MMfngVwtpVMqVrwrMBgmtGqCHDWqJSDJWhHHSSSJJHHD\n" +
                "tBgnMTMMrgVmrBwMmGfnNjjsdLbbbTQvjNTNsQLz\n" +
                "ZZBZRmPmgpgZGLWLQWslSWmLQL\n" +
                "DnHJJjzqrJffrDnHzJjnMbQWSltttSbStvFQSstSvCLF\n" +
                "MzJDnfzHwHlljJJnqrMjfPGdBRpRBGBRhwVdGGRTBG\n" +
                "CnZCpMFNnFvvNdpHVrWghgtFVFlLRWhh\n" +
                "cBsSBsGcjGcJZDrggtgtVDVrgWmh\n" +
                "wTBJbcbzffJbZccjSbSjBfccNCNMPqqPPdvnHvTvnMTNdnvQ\n" +
                "vMgPmvQmWDMpGpjBbMMH\n" +
                "CcVJNcdNgdhtCVpjBBRppfRTGbph\n" +
                "sFsgNlcdFlJFFwFstNJcvzDWZqqWvqLqzLzmzDwQ\n" +
                "LLVLVsPPVVPCLLrjCNNNgmRdJNdCdfMJpB\n" +
                "DTZZHTWbwwpWbSWDBmJMSFFNmgRRBggf\n" +
                "ZvzDWqDnDwnZTpzZTzWvphPtqhQsltVtPhPhsQrPch\n" +
                "zDgWmDgrpCLmwgWTrjlJBQRJjbFGrcbQ\n" +
                "hSMvqvHtqsdVHlJDcclMBjRMQJ\n" +
                "sqvHsSstSdqhVVvZdqVHZDgwWpZZLLmfmmwfNfWCgmLg\n" +
                "SQWcTnWVWbZWWBcVPnZVbnrNrMFMdqFNqdMqqFhrDQvq\n" +
                "plGLlLGpJLhCGrRqGDDDrdzNGr\n" +
                "wgflHCCCJmpLjCLHtjjgLCtBZswnsTBPVPVsBcPTbZBBSh\n" +
                "vvlMQvvdjdGtVCTJlVJVfJ\n" +
                "FLrFqwwZgNrFWqZwgqrZBLWcBTtppztVbfRJztJbztfztT\n" +
                "WNmmFJwwrFFnNmDgmjdGQMdHMsPvPjsHDG\n" +
                "hGmZHdSRdMmhMZSHlvbTvRbRlVtCTlCR\n" +
                "znnfzgPPDpPfDcgnZTJvJNCZbJVCcNJV\n" +
                "nrLLfQznprrppgprWrnPzQzLSjGsZmHmhBdsqWhdhBMWhdqd\n" +
                "zhtNFSFwRFLCsNrNNBdl\n" +
                "BmQBPjDpBTDgHllgHc\n" +
                "npBjjpQpjGbMnmPpjPQWpwZhtbzJfhwvwtSwhhFFbh\n" +
                "PZcZbcPlbSprcQbbdCwWRSttgtgvWfjC\n" +
                "TGVLVHHmTVHGDTDnGDhgWjwvCjwwwRLLgBjWBR\n" +
                "CHTGsnHVVcJPPcNsNJ\n" +
                "tTqGSSGPGfVfTpqGTbbcVWJLdjtvdzjJthCjlhdlzQ\n" +
                "wwFBZMmZBmgnjzlCWBBjBLjv\n" +
                "rNMsDZnMMWSfDcDWPR\n" +
                "vLzbsczhLmmnlNvrNQHfWd\n" +
                "SMSFqMwjFFDVSZwVTMDjSQlQfNlRrQRWdQfRrWrqHN\n" +
                "CPTwGZDTFCPSjFTSPSFbPgpLscPczmcBLbfgpb\n" +
                "QnQnpFjsbFcSSvCMNvqVSrqq\n" +
                "WfzfTfzzPgHTfwfWtgRLMJDvjMmMVtvDJJCVtqmC\n" +
                "wfWRgPzdgRTWBBWHPBHHBRLTlcZdhjnbZQcGZGpsnphjshbG\n" +
                "pHzPTsBHzqqtQCZZshlWjf\n" +
                "DFFbnvJMDMljjtQjfCbQ\n" +
                "dgJFDGwgmGlMSggGdgdDDlvLNTzpBzLzzwpTBLzqPBczLT\n" +
                "jccNVNdwnclRwlbwlVjdcpJSpGpSllBHgGHZpJpppf\n" +
                "mDThTmsnDsSBpZfmmgBf\n" +
                "MrFrhCshqvWvnWzTWQtzVbRRQwQRNQjdwQ\n" +
                "tBnLJfnQtzRCffmNjSRjZjNZSRrP\n" +
                "dVdMVMvMghHzPhzZhHND\n" +
                "dGWGgplWGVMdMMzCTsbLtLTCLpnT\n" +
                "ftNfNDdSBdrMTdrjMM\n" +
                "cHgHGHzGgJhrPLqSrrJTqp\n" +
                "mVFnQnhQGHFznFhBBbSDRBlSVBBRfS\n" +
                "VqqPBPcPbQHgfrrpcSDR\n" +
                "tpMnsztnGnthhzTtGTGTzzWgJNDlMfSRlRDgRNRrDRHfrg\n" +
                "zWtTFWzTwphChnCzFhzWZGGvBvLqmVmbVQqjqjmBPqBLCP\n" +
                "ZZgZnhrmwmnmgmvrghPmgTGcTSGSMSldgcCQCSqW\n" +
                "LzFLDBfHzHCCqCFGcSlS\n" +
                "HBjRJDLpHpJsJVJqsnhP\n" +
                "PqrqmvmrwzznnPDpjVpDLfDtPGLt\n" +
                "sdRhRWFhShhFccZZsSsNbsNcjCtLpMVWCjptGCfMftBDLMtG\n" +
                "bVZcsdlhdNSbZRSshRcbbqlmnqHmmwzrJlzzgQlmvz\n" +
                "pnrcNGqmrGqnchGhqdWdTlldtQtlMsTq\n" +
                "DvSLgzLSMfbgggCLCwbSSLLtfsWTQTsWllssdltRQQtttQ\n" +
                "bCCzzPPgDPjPvwSzDbwpVNnpnjjrhpnVZGMhcp\n" +
                "jWbGtDdqCqZjdHwcwZMBVQmcvZ\n" +
                "PnTflPRRrlgLTTRlTzFPPQQBcNvHBncQpHMwHNBMwm\n" +
                "fFFRrFLJgRcJglgRzTzrLqWCjtqGGDsjCjdbGdqdhJ\n" +
                "GwbvGqMsDMbpMGzzgRzgpBLjhcch\n" +
                "WFTFNZTZSCcBggBFcrss\n" +
                "CJWWlsWlCtqGJmMGwJ\n" +
                "CGCVhprTrthCZTCNtVGtZDZNdlPPdPwmmvrcbmPmdQRvQWmw\n" +
                "LfzLzssfgHjLFjFLfjMfHsLHmPwdcQWQQlscwlPdQclbPvlw\n" +
                "LBFHjgMzqqjfJqLMzffHzqgHhhJDZSGVDVChCDDpDNNpNtDW\n" +
                "TbzVlmNTVVtnTSWNwDDrpGcwdp\n" +
                "fQQMFbhCfLgfQCsdDcHpsWpdSDsGrr\n" +
                "ghvPLQMfZhjjvPLhbQFQBZqJlTnnnVzRmtRzlmBl\n" +
                "JCLLLwVDwCQsNwwJHmfrMZpMfMMrfPQSMZpS\n" +
                "WlFlzFRnznthqWRGbMpVMbbMPtMjMj\n" +
                "vTnvzqllhdhqTwVBLcJHmmmC\n" +
                "tczhtcJJJbtclWrtJBWJBtJtpqPRSPfpBRgqRfPmpRqddSmM\n" +
                "HCvnsQLNCQwLnDsNHLwQfPSSpPSMfnPddRMmmGpp\n" +
                "wDQwjNwQNHjTHNFDCNmCFNWtWzhJbWbVrhtWccVFlrlV\n" +
                "sPRpCndBCGpCGHttSdvTbWvgdjST\n" +
                "wcmDwqcwmGDTNvjWtrbSrc\n" +
                "lwlVLVGqZGlLzVHHBBBCHBHRPCCz\n" +
                "wdmhffzzphrjqtzRbrrq\n" +
                "CRgGTGTFssZsllHNBlHsFJRjcrtjtPDPcbCtDrLcrjctrc\n" +
                "NHMRHTlFgGNwpQvMpwVvww\n" +
                "MPLJNPqmFWmDFjGS\n" +
                "nbsZtwbZlbZlGlFDDMpVlF\n" +
                "hvsbbbZtvfhhRZbZsfzMbMZbqcrqdrNrNqLgqhrLhJgddLNL\n" +
                "SnMLpRDGlZSZNlnMZpCwjLwzFrHBWCFWBBBr\n" +
                "TttvvtbtVcsJtRsvtQdzWJrBjCCHBWzrFFhCjC\n" +
                "VmvsQdgPbdgVTvgPMSDfPPZfDRRNDNMl\n" +
                "LjngLCNhDNFNhFDhcMqrqqZMcSZnHTMc\n" +
                "PPJwtGlfszGwWtzwQJBPGslJSqRTHZvgcRRZrMSTMMTtRTTc\n" +
                "llPPJWzQPmWmVNgDbLFCLb\n" +
                "NPFlLNBLprpdmmdPBmJnLrdjMVDjMSdqgggQTVDqWMdqVs\n" +
                "vZTbTZRwvvGRTRjWDqSqqQgDGsGq\n" +
                "vzZcfRRZbwbRHRtwZCChBmFNtJBPLBlBJJLpmFTP\n" +
                "pmvZmmTjQFfnvPPHHv\n" +
                "SczhzfbsLNhfccNFsWFRPrDnPDnVnW\n" +
                "BtBbSdtzLBwSLwBmTZpQMpZmZmfZ\n" +
                "PqPQZqtQQLDqrnqdjqdVwVbz\n" +
                "MGRGWMgJHGlRRHfSwfzCfCVVQzbwjrjn\n" +
                "JsmHmSJJmSMWMlTWQBFhLTvhDFZhBQDZ\n" +
                "sbgbbFGTTFNMbMNFWrjsrvWzHWPzPPpf\n" +
                "CVmhVqSqCZmJQhPpHzvZvtzWHjHP\n" +
                "CnmdCQCdnFTnNgRpwT\n" +
                "blZjhbZWVttjWjWLCLVVZCZQjMDQHsBsBQfMDQwjHDwBHH\n" +
                "NdcJdFcJqgpJpNnDQLMFsBnLSnnS\n" +
                "LJrJdJrzvdrrpcNdNcrVlZWbZzZVRhRtVlPttC\n" +
                "mhRtNNtrtBQQrtrBBmQlZwHHqHZSVHHGshSVDwhS\n" +
                "gpdPMTcsLscMccTpbLdHSfGfqwHZDHHqZqHZ\n" +
                "zbzvMpPLppLzLMjTBQRmssjBWRQjlmrN\n" +
                "VzzvggdvFdmffwmGpd\n" +
                "HNbnJTRTmCwwrRpR\n" +
                "LlTnWhLlhLJmLmtZtPcPcVFFPSZgZt\n" +
                "jHcZjHlHzLHHnSNSfL\n" +
                "pQWRrwPwrRWBWBPWBRrpdPmzhShsSFFNShLhnnvPtvSNNs\n" +
                "dzbmwVwbbBmGcqDbgllJCC\n" +
                "ndnvvzJDHvzHHHjnHjCCSDLgbSFwNFVbFVTL\n" +
                "mcQmQtpWTQGlmpTtMtqtpqTFsLcVSSscNCwLNLbwbbLNwV\n" +
                "pRZTQlhmtGWqqWnPHdnhjHrBjPPd\n" +
                "TtLpNHspTcLNNsLpthhsfmtjRSRlWWbzSwSRGwbWlWSSvlmS\n" +
                "qBJVnZZdJVZrZndbPbWwRzSMVGbbVS\n" +
                "QCdnBFBndBQDnrqrnqqNhpNNLpHthsThjGCTLL\n" +
                "phCgcdrFbPLpgrbFHqQqzzlbGWGqQbHW\n" +
                "SFTvTnVVMRnNTNfSHjHQMDlHwDWlQwDz\n" +
                "TZmTvsFNmvTtsggpdJLBBsCs\n" +
                "PBBWQjvsPsHVsNMcSzNDjcGggS\n" +
                "ZtrTfTrrrrdCqpdtLNnMLLqNcgMzgHLq\n" +
                "CZFmdTrJtbZrBvWHVVvHbPQW\n" +
                "djcrrBljMrTdCTcdCClClMlqRvtNqqSRwFbNbwvNBNpSzq\n" +
                "QhPmGJnPVGVHHNzSqpzFwztF\n" +
                "nhgPFmsnLPGLhPDJhGTcDjMfrMMjMZWfjfWj";
    }
}
